'''
Created on 2016年6月26日

@author: cheng
'''
cl = []
import tornado.websocket
import tornado.web
import json
import redis
import app_global


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        response_to_send={}
        
        try:

            self.handle_message(message,response_to_send)
            
        except IOError:
            
            response_to_send["status"]={"error":"500"}
            
        self.write_message(json.dumps(response_to_send))

    def open(self):
        if self not in cl:
            cl.append(self)
            #self.write_message(u"Connected")
            app_global.clients_monitor_count += 1
         
            print("Rh WS open " + str(len(cl)) + " Total Client: ", str(app_global.clients_monitor_count))

    def on_close(self):
        if self in cl:
            cl.remove(self)
            app_global.clients_monitor_count -= 1
            print("Rh WS close " + str(len(cl)) + " Total Client: ", str(app_global.clients_monitor_count))
    
    def handle_message(self,message,response_to_send):
        
        req=json.loads(message)
        if( req.get("request") not in app_global.CLIENT_REQ_TYPES.keys()):
                response_to_send["status"]={"error":"502"}
        else:
            
            self.handle_req_type(req)
           
            response_to_send["status"]="OK"
            
    def handle_req_type(self,req):
        
        app_global.CLIENT_REQ_TYPES[req['type']]()
        
class ApiHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, *args):

        uid = self.get_argument("id")
        value = self.get_argument("value")
        name=uid+"."+value
        payload = app_global.redisClient.get(name)
        if payload is not None:
            data = {"id": uid, "value" : payload.decode()}
        else:
            data={"error":name + " not found"}
        self.write(data)
        self.finish()



    @tornado.web.asynchronous
    def post(self):
        pass