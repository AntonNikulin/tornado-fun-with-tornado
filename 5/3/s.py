import os.path

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado.options
from uuid import uuid4

class Counter(object):
    count = 10
    observers = []

    def add(self, number = 1):
        self.count += number

    def registerObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        for observer in self.observers:
            print observer
            observer.valueChanged()

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        count = self.application.counter.count
        self.render("index.html", count = count)

class WsHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "conn open"
        if self not in self.application.counter.observers:
            self.application.counter.registerObserver(self)

    def on_message(self, message):
        self.application.counter.add(int(message))
        self.application.counter.notifyObservers()

    def valueChanged(self):        
        count = str(self.application.counter.count)
        self.write_message(count)

class Application(tornado.web.Application):
    def __init__(self):
        self.counter = Counter()
        handlers = [
            (r'/', IndexHandler),
            (r'/counter', WsHandler),
            (r'/counter/add', WsHandler)
        ]        
        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "static")
        }
        tornado.web.Application.__init__(self, handlers,debug=True, **settings)
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
