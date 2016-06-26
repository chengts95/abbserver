# -*- coding: utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

import os
import app_global
import tornado.autoreload
import basic_handler
import api_handler

class IndexHandler(basic_handler.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html',title="dashborad", user=self.current_user)


class realtimeHandler(basic_handler.BaseHandler):
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
             (r'/ws', api_handler.WebSocketHandler),
             (r'/api', api_handler.ApiHandler),
            (r'/', IndexHandler),
            (r'/logout', basic_handler.LogoutHandler),
            (r'/login', basic_handler.LoginHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url="/login",
        )

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':


    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
