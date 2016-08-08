'''

用来定义各种常量

Created on 2016年6月26日

@author: cheng
'''
AC_TYPE = "AC"
SENSOR_TYPE = "SENSOR"
PERF_TYPE = "PERF"
GET_REQ = "GET"
UPDATE_REQ = "POST"
SET_REQ = "SET"
DEL_REQ = "DELETE"
AC_DEFAULT_PROPS = {
    "type": AC_TYPE,
    "name": "genertic ac",
    "set_temp": {"value": 26, "q": 0},
    "room_temp": {"value": 26, "q": 0},
    "power": {"value": 0, "q": 0},

}
SENSOR_DEFAULT_PROPS = {
    "type": SENSOR_TYPE,
    "name": "genertic sensor",
    "temp": {"value": 26, "q": 0},
    "humid": {"value": 20, "q": 0},
    "power": {"value": 0, "q": 0}

}
PERF_DEFAULT_PROPS = {

    "type": PERF_TYPE,
    "name": "genertic person",
    "pefer_temp": {"value": 0, "q": 0}

}


DATA_TYPES = {AC_TYPE: AC_DEFAULT_PROPS,
              SENSOR_TYPE: SENSOR_DEFAULT_PROPS,
              PERF_TYPE: PERF_DEFAULT_PROPS}

CLIENT_REQ_TYPES = {
    GET_REQ: lambda: print("GET"),
    UPDATE_REQ: lambda: print("UPDATE"),
    SET_REQ: lambda: print("SET")
}
