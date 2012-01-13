from base import BaseHandler

class TextHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/text" method="post">'
                   '<input type="text" name="text">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
        
    def post(self):
        self.write("text handler!")
        text = self.request.arguments['text'][0]
        
        req = tornado.httpclient.HTTPRequest( url=_text_url, method="POST",body="apikey="+_text_api_key+"&text="+text,
                                              validate_cert = False)
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(req, self.handle_response)

    def handle_response(self):
        self.save_text_analysis(response)
