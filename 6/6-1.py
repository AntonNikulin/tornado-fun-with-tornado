import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		cookie = self.get_secure_cookie("count")
		count = int(cookie) + 1 if cookie else 1

		countString = "1 time" if count == 1 else "%d times" % count

		self.set_secure_cookie("count", str(count))

		self.write("""
			<html>
				<head>
					<title>Cookie Counter</title>
				</head>
				<body>
					<h1>You've viewed this page %s times.</h1>
				</body>
			</html>""" %count
		)
if __name__ == "__main__":
	tornado.options.parse_command_line()

	settings = {
	"cookie_secret": "ss4jlskdfL4_34/ll9="
	}

	application = tornado.web.Application([
		(r"/", MainHandler)
		], debug=True, ** settings)
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8000)
	tornado.ioloop.IOLoop.instance().start()
