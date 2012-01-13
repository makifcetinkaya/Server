import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.httpclient
import tornado.httputil
from home import HomeHandler
from text import TextHandler
from picture import PictureHandler
from reg import RegHandler
from login import LoginHandler
from logout import LogoutHandler
from eda import EDAHandler
          
        
application = tornado.web.Application([
    (r"/", HomeHandler),
    (r"/text", TextHandler),
    (r"/picture", PictureHandler),
    (r"/reg", RegHandler),
    (r"/login",LoginHandler),
    (r"/logout",LogoutHandler),
    (r"/eda", EDAHandler),
], cookie_secret='UcCbwfNHSoSUQKnC6gVhR/+nKf4MIUxruhq3buIEkYk=' )

    
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    
