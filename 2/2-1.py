import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

class CalcPageHandler(tornado.web.RequestHandler):
	def post(self):
		var1 = self.get_argument("var1")
		var2 = self.get_argument("var2")
		res = int(var1) + int(var2)
		d ={"var1": var1, "var2": var2, "res": res}
		self.render("result.html", var1 = var1, var2 = var2, res= res)

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[(r"/", IndexHandler),(r"/calc", CalcPageHandler)],
		template_path = os.path.join(os.path.dirname(__file__), "templates")
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
