import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
	def get(self, input):
		self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
	def post(self):
		text = self.get_argument('text')
		width = self.get_argument('width', 40)
		self.write(textwrap.fill(text, width))

class TestHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("And this is a get")

	def head(self):
		self.set_status(400)

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[
		(r"/test", TestHandler),
		(r"/reverse/(\w+)", ReverseHandler),
		(r"/wrap", WrapHandler)
		]	
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()