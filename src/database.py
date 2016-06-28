'''
Created on 2016年6月26日

@author: cheng
'''
from datadef  import *
import redis
import time
import json
import traceback
redisClient=redis.StrictRedis(host='127.0.0.1',port=6379,db=0,
                              decode_responses=True)
DEFAULT_STATUS={e:0 for e in DATA_TYPES.keys() }

GET_PROP="prop"
GET_HISTORY="history"


def init_data():
    redisClient.flushdb()    
    if(redisClient.hgetall('STATUS')=={}):    
        redisClient.hmset('STATUS', DEFAULT_STATUS)
    

def get_props_by_name(data):
    pipe=redisClient.pipeline()
    respond_to_send={}
    for dname in data.keys():
         
        if redisClient.hexists('NAMES', dname):
             
                pipe.hget("NAMES",dname)
       
                
    temp=pipe.execute()      
    for item in temp:
        name=item
        pipe.hgetall(name)
    
    temp2=pipe.execute()
    for item in temp2:
        print(item)
        respond_to_send[item['name']]=item
    return respond_to_send

def get_time(seconds):
    return time.ctime(eval(seconds))
      
def get_data(data):
    pipe=redisClient.pipeline()
    respond_to_send={}
    try:
        for dname in data.keys():
             
            if redisClient.hexists('NAMES', dname):
                respond_to_send[dname]=redisClient.hget("NAMES",dname)
        
        for item in respond_to_send.keys():
            name=respond_to_send[item]
            
            start=data[item].get('s_ts')
            end=data[item].get('e_ts')
            if  start is  None or end is None:
                pipe.zrange('%s.DATA'%name, -1, -1,  withscores=True,
                                    score_cast_func=get_time)
            else:
                pipe.zrangebyscore('%s.DATA'%name, float(start), float(end),  withscores=True,
                                    score_cast_func=get_time)
           
            
        l=pipe.execute()
        counter=0
        for item in respond_to_send.keys():
            respond_to_send[item]=l[counter]
            counter+=1
    except redis.exceptions.ResponseError:
            print(traceback.format_exc())
            respond_to_send[dname]="error"
    return respond_to_send    
    
GET_TYPE={GET_PROP:get_props_by_name,
          GET_HISTORY:get_data
            }    

def get_key(req):
    NOT_FOUND=-1
   
    data=req.get('payload') 
    type=req.get('type') 
    if data == None or type == None:
        return NOT_FOUND
    else:
        if type in GET_TYPE.keys():
            return GET_TYPE[type](data)
        
      
    

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
                    uid=redisClient.hincrby('STATUS',"%s:total"%dt)
                    pipe=redisClient.pipeline()
                    pipe.hset('NAMES', dname, dt+str(uid))
                    temp['id']=uid
                    pipe.hmset(dt+str(uid),temp)
                    pipe.execute()   
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
                pipe.zadd("%s.DATA"%key,data[dname]['ts'],data[dname])
            else:
                pipe.delete()
                return NOT_FOUND#duplicated           
        pipe.execute()      
    return 1        

CLIENT_REQ_TYPES={GET_REQ:get_key,
                  UPDATE_REQ:update_key,
                  SET_REQ:set_key}
init_data()
