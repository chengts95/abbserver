from database import *
from datadef  import *

clients_machine_ip = []
clients_monitor_count = 0



def get_key(req):
    
    pass

def set_key(req):
    pass

def update_key(req):
    pass    

CLIENT_REQ_TYPES={GET_REQ:get_key,
                  UPDATE_REQ:update_key,
                  SET_REQ:set_key}