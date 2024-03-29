from feel_base import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):
        if(self.is_user_logged_in()):
            self.write('<html><body><p>Enter text:</p><form action="/text" enctype="multipart/form-data" method="post">'
                    '<input type="text" name="text">'
                    '<input type="submit" value="Submit">'
                    '</form><p>Upload a picture:</p><form action="/picture" enctype="multipart/form-data" method="post">'
                   '<input type="file" name="picture">'
                   '<input type="submit" value="Upload">'
                   '</form><p>Upload EDA data:</p><form action="/eda" enctype="multipart/form-data" method="post">'
                   '<input type="file" name="eda">'
                   '<input type="submit" value="Upload">'
                   '</form>' 
                    '<form action="/logout" method="GET">'
                       '<input type="submit" name="Logout" value="Logout">'
                       '</form>'
                    '</body></html>')
        else:
            self.redirect('/login')
