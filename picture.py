from base import BaseHandler
import face_client
from database import Database as db

_face_api_key="9f5766905329451c675eb672a201d611"
_face_api_secret= "12fd4aba022424d195c4317459c4bf1f"

class PictureHandler(BaseHandler):

    def get(self):
        self.write('<html><body><form action="/picture" method="post" enctype="multipart/form-data">'
                   '<input type="file" name="picture">'
                   '<input type="submit" value="Upload">'
                   '</form>'
                   '</body></html>')
    def post(self):
        self.write("pic handler!")
        pic_name = self.request.files.get("picture")[0]['filename']       
        client = face_client.FaceClient(api_key=_face_api_key,api_secret=_face_api_secret)
        response = client.faces_detect(urls=None, file_name=pic_name)
        self.handle_response(response)

    def handle_response(self, response):
        return self.save_picture_analysis(response)
        
