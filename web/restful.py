# -*- coding: utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.websocket
import json
import redis
import os
import app_global

import tornado.autoreload

cl = []
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html',title="dashborad", user=self.current_user)


class LoginHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        incorrect = self.get_secure_cookie("incorrect")
        if incorrect and int(incorrect) > 25:
            self.write('<center>blocked</center>')
            return
        self.render('pages/login.html')

    @tornado.gen.coroutine
    def post(self):
        username = tornado.escape.xhtml_escape(self.get_argument("username"))
        password = tornado.escape.xhtml_escape(self.get_argument("password"))
        if "ID002" == username and "123456" == password:
            self.set_secure_cookie("user", self.get_argument("username"))
            self.set_secure_cookie("incorrect", "0")
            self.redirect("/")

        else:
            incorrect = self.get_secure_cookie("incorrect")
            if not incorrect:
                incorrect = 0
            self.set_secure_cookie("incorrect", str(int(incorrect)+1))
            self.write('<center>Something Wrong With Your Data <a href="/">Go Home</a></center>')

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/"))

class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        print("message received " + message)
        response_to_send={}
        try:

            taggroup=message

            tags=[taggroup+'.TS',taggroup+'.NAME',taggroup+'.GY',taggroup+'.DY',taggroup+'.MB']
            for a in tags:
                response_to_send[a]={}
                response_to_send[a]["value"]=app_global.redisClient.get(a).decode()
        except IOError:
            response_to_send["error"]="500"
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

class realtimeHandler(BaseHandler):
    @tornado.web.authenticated
    @tornado.gen.coroutine
    def get(self, *args):
        taggroup=self.get_argument("tag")

        title=u'在线监测'
        groupname=app_global.redisClient.get(taggroup+".NAME")
        if groupname is not None:
            groupname=groupname.decode()
            tagnames=self.get_tags(taggroup)
            self.render("test2.html",svg="/static/svg/bpr.min.svg",groupname=groupname,title=title,tagnames=tagnames)
        else:
            self.write('<center>The group is not esxit!<a href="/">Go Home</a></center>')

    def get_tags(self,taggroup):

        tags=[taggroup+'.TS',taggroup+'.NAME',taggroup+'.GY',taggroup+'.DY',taggroup+'.MB']
        return  tags

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
             (r'/monitor', realtimeHandler),
             (r'/ws', WebSocketHandler),
             (r'/api', ApiHandler),
            (r'/', IndexHandler),
            (r'/logout', LogoutHandler),
            (r'/login', LoginHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url="/login",
        )

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
#    app.listen(8888)
#    ioloop.IOLoop.instance().start()

    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
