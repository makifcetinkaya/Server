from base import BaseHandler

class EDAHandler(BaseHandler):
    def get(self):
        self.write('eda handler!')
    def post(self):
        pass
