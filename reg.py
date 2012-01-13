from base import BaseHandler

class RegHandler(BaseHandler):
        def get(self):
            if self.is_user_logged_in():
                self.redirect("/")
                return
            self.write('<html><body><form action="/reg" method="post">'
                   '<p>Email:<p/><input type="text" name="email"/>'
                   '<p>Password<p/><input type="password" name="password"/>'
                    '<p>Password Confirm</p><input type="password" name="password"/>'
                    '<input type="submit" name="submit"/>'
                   '</form></body></html>')
        def post(self):
            email = self.request.arguments['email'][0]
            password = self.request.arguments['password'][0]

            if self.register(email, password):
                    self.write("registered successfully")
                    self.redirect('/')
            else:
                    print "could not register"
                    self.redirect('/reg')
