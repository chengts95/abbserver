'''
Created on 2016年6月26日

@author: cheng
'''
from datadef  import *
import redis
import time
redisClient=redis.StrictRedis(host='127.0.0.1',port=6379,db=0)

DEFAULT_STATUS={e:0 for e in DATA_TYPES.keys() }


def init_data():
    redisClient.flushdb()    
    if(redisClient.hgetall('STATUS')=={}):    
        redisClient.hmset('STATUS', DEFAULT_STATUS)
     
    


def get_key(req):
    
    pass

def set_key(req):
    NOT_FOUND=-1
    data=req.get('payload') 
    if data == None :
        return NOT_FOUND
    else:
        for dname in data.keys():
             
            if not redisClient.hexists('NAMES', dname):
            
                dt = data[dname].get('type')
                
                if dt in DATA_TYPES.keys():
                    
                    temp=DATA_TYPES[dt].copy()
                    temp['name']=dname
                    for k in data[dname].keys():
                        temp[k]=data[dname][k]
                    redisClient.hincrby('STATUS',"%s:total"%dt)
                    redisClient.hset('NAMES', dname, dt+str(1))
                    redisClient.hmset(dt+str(1),temp)
                    
                else:
                    return NOT_FOUND
            else:
                return -2#duplicated
    return 1        
    

def update_key(req):
    NOT_FOUND=-1
    data=req.get('payload') 
    if data == None :
        return NOT_FOUND
    else:
        pipe=redisClient.pipeline()
        for dname in data.keys():
            key=redisClient.hget('NAMES', dname)
            if key != None:
                data[dname].setdefault('ts',time.time())
                pipe.zadd("%s.DATA"%key.decode(),data[dname]['ts'],data[dname])
            else:
                pipe.delete()
                return NOT_FOUND#duplicated           
        pipe.execute()      
    return 1        

CLIENT_REQ_TYPES={GET_REQ:get_key,
                  UPDATE_REQ:update_key,
                  SET_REQ:set_key}
init_data()
