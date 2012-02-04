from feel_eda import EDAHandler
from feel_home import HomeHandler
from feel_login import LoginHandler
from feel_logout import LogoutHandler
from feel_picture import PictureHandler
from feel_reg import RegHandler
from feel_text import TextHandler
from feel_calendar import CalendarHandler

import tornado.ioloop
import tornado.web
          
        
application = tornado.web.Application([
    (r"/", HomeHandler),
    (r"/text", TextHandler),
    (r"/picture", PictureHandler),
    (r"/reg", RegHandler),
    (r"/login",LoginHandler),
    (r"/logout",LogoutHandler),
    (r"/eda", EDAHandler),
    (r"/calendar", CalendarHandler),
], cookie_secret='UcCbwfNHSoSUQKnC6gVhR/+nKf4MIUxruhq3buIEkYk=' )

    
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    
