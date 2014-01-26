import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class TestHandler(tornado.web.RequestHandler):
	def write_error(self, status_code, **kwargs):
		self.write("Freakin unbelievable {0} error. Why did you do that?"
			.format(status_code))

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[
		(r"/test", TestHandler),
		]	
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()