from base import BaseHandler
import base64, uuid

class LoginHandler(BaseHandler):
    def get(self):
        
        if self.is_user_logged_in():
            self.redirect("/")
            return
        self.write('<html><body><form action="/login" method="post">'
                   '<p>Email:<p/><input type="text" name="email"/>'
                   '<p>Password<p/><input type="password" name="password"/>'
                   '<input type="submit" name="Login" value="Login"/>'
                   '</form>'
                    '<form action="/reg" method="get">'
                   '<input type="submit" value="Register"/>'
                   '</form>'
                   '</body></html>')
    def post(self):
        email = self.request.arguments['email'][0]
        password = self.request.arguments['password'][0]
        
        if self.is_correct_login(email, password):
            key = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
            if(self.save_login(email, key)):
                self.write("successful login")
                self.set_secure_cookie('key', key)
                self.redirect("/")
            else:
                self.write("could not login=(")
                self.redirect('/login')
        else:
            print "incorrect login"
            self.redirect('/login')
