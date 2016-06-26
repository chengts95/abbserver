'''
Created on 2016年6月26日

@author: cheng
'''
AC_TYPE="AC"
SENSOR_TYPE="SENSOR"
PERF_TYPE="PERF"
GET_REQ="GET"
UPDATE_REQ="POST"
SET_REQ="SET"

CLIENT_REQ_TYPES={GET_REQ:lambda :print("GET"),
                  UPDATE_REQ:lambda :print("UPDATE"),
                  SET_REQ:lambda :print("SET")}

AC_DEFAULT_PROPS={"type":AC_TYPE,
          "name":"genertic ac",
          "set_temp":26,
          "room_temp":26,
          "power":0
          }
SENSOR_DEFAULT_PROPS={"type":SENSOR_TYPE,
          "name":"genertic sensor",
          "temp":26,
          "humid":26,
          "power":0
          }
PERF_DEFAULT_PROPS={"type":PERF_TYPE,
          "name":"genertic person",
          "pefer_temp":26
          }


class air_condition:
    
    def __init__(self,tag,id,name="genertic ac",
             set_temp=26,room_temp=26,power=0):
        self.tag=tag
        self.id=id
        self.name=name
        self.type=AC_TYPE
        self.set_temp=set_temp
        self.room_temp=room_temp
        self.power
 
 