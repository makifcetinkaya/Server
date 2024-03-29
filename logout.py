from base import BaseHandler

class LogoutHandler(BaseHandler):
    def get(self):
        if self.logout():
            self.clear_all_cookies()
            self.redirect('/login')
        else:
            self.write("problem loggin out..")
            self.redirect('/')
