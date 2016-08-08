'''
Created on 2016年6月26日

@author: cheng
'''
from datadef import *
import redis
import time
import json
import traceback
import os


class redis_client:

    GET_PROP = "prop"
    GET_HISTORY = "history"

    def __init__(self, host='127.0.0.1', port='6379'):

        self.GET_TYPE = {
            self.GET_PROP: self.get_props_by_name,
            self.GET_HISTORY: self.get_data
        }
        self.host = host
        self.port = port

        self.redisClient = redis.StrictRedis(host=host, port=port, db=0,
                                             decode_responses=True)
        self.DEFAULT_STATUS = {e: 0 for e in DATA_TYPES.keys()}

        self.GET_PROP = "prop"
        self.GET_HISTORY = "history"

    def init_data(self):
        self.redisClient.flushdb()
        if(self.redisClient.hgetall('STATUS') == {}):
            self.redisClient.hmset('STATUS', self.DEFAULT_STATUS)

    def get_props_by_name(self, data):
        pipe = self.redisClient.pipeline()
        respond_to_send = {}
        for dname in data.keys():

            if self.redisClient.hexists('NAMES', dname):

                pipe.hget("NAMES", dname)

        temp = pipe.execute()
        for item in temp:
            name = item
            pipe.hgetall(name)

        temp2 = pipe.execute()
        for item in temp2:
            print(item)
            respond_to_send[item['name']] = item
        return respond_to_send

    def get_time(self, seconds):
        return time.ctime(eval(seconds))

    def get_data(self, data):
        pipe = self.redisClient.pipeline()
        respond_to_send = {}
        try:
            for dname in data.keys():

                if self.redisClient.hexists('NAMES', dname):
                    respond_to_send[dname] = self.redisClient.hget("NAMES", dname)

            for item in respond_to_send.keys():
                name = respond_to_send[item]

                start = data[item].get('s_ts')
                end = data[item].get('e_ts')
                if start is None or end is None:
                    pipe.zrange('%s.DATA' % name, -1, -1,  withscores=True,
                                score_cast_func=get_time)
                else:
                    pipe.zrangebyscore('%s.DATA' % name, float(start), float(end),  withscores=True,
                                       score_cast_func=get_time)

            l = pipe.execute()
            counter = 0
            for item in respond_to_send.keys():
                respond_to_send[item] = l[counter]
                counter += 1
        except redis.exceptions.ResponseError:
            print(traceback.format_exc())
            respond_to_send[dname] = "error"
        return respond_to_send

    def get_key(self, req):
        NOT_FOUND = -1

        data = req.get('payload')
        dtype = req.get('type')
        if data == None or dtype == None:
            return NOT_FOUND
        else:
            if type in self.GET_TYPE.keys():
                return self.GET_TYPE[dtype](data)

    def set_key(self, req):
        NOT_FOUND = -1
        data = req.get('payload')
        if data == None:
            return NOT_FOUND
        else:
            for dname in data.keys():

                if not self.redisClient.hexists('NAMES', dname):

                    dt = data[dname].get('type')

                    if dt in DATA_TYPES.keys():

                        temp = DATA_TYPES[dt].copy()
                        temp['name'] = dname
                        for k in data[dname].keys():
                            temp[k] = data[dname][k]
                        uid = self.redisClient.hincrby('STATUS', "%s:total" % dt)
                        pipe = self.redisClient.pipeline()
                        pipe.hset('NAMES', dname, dt + str(uid))
                        temp['id'] = uid
                        pipe.hmset(dt + str(uid), temp)
                        pipe.execute()
                    else:
                        return NOT_FOUND
                else:
                    return -2  # duplicated
        return 1

    def update_key(self, req):
        NOT_FOUND = -1
        data = req.get('payload')
        if data == None:
            return NOT_FOUND
        else:
            pipe = self.redisClient.pipeline()
            for dname in data.keys():
                key = self.redisClient.hget('NAMES', dname)
                if key != None:
                    data[dname].setdefault('ts', time.time())
                    pipe.zadd("%s.DATA" % key, data[dname]['ts'], data[dname])
                else:
                    pipe.delete()
                    return NOT_FOUND  # duplicated
            pipe.execute()
        return 1

host = os.getenv("REDIS_IP", "127.0.0.1")
port = os.getenv("REDIS_PORT", "6379")


def init_redis():
    global CLIENT_REQ_TYPES, GET_REQ, UPDATE_REQ, SET_REQ
    r = redis_client(host,port)
    CLIENT_REQ_TYPES = {GET_REQ: r.get_key,
                        UPDATE_REQ: r.update_key,
                        SET_REQ: r.set_key}
init_redis()
