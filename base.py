import tornado.web
from database import Database as db

cursor = db.cursor

class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("key")

    def is_user_logged_in(self):
        key = self.get_current_user()
        if key:
            query = "SELECT * FROM login WHERE `key`='{}' LIMIT 1".format(key)
            if self.safe_execute(query):
                result = cursor.fetchone()
                return (result!=None)

        return False
       
    def is_correct_login(self, email, password):
        print "checking if cor login"
        query = "SELECT * FROM user WHERE `email`='{}'".format(email)
        cursor.execute(query)
        result = cursor.fetchone()
        if(result != None):
            if (result[2] == password):
                return True
        return False
                   
    def save_login(self, email, key):
        query = "INSERT INTO login (`email`, `key`) VALUES ('{0}','{1}')".format(email, key)
        return self.safe_execute(query)
    
    def logout(self):
        query = "DELETE FROM login WHERE `key`='{}'".format(self.get_current_user())
        return self.safe_execute(query)
        
    def register(self, email, password):
        print "attempting to register"
        print email, password
        query = """INSERT INTO user (`email`, `password`)
                        VALUES ('{0}', '{1}')""".format(email, password)
        return self.safe_execute(query)
                
    def save_picture_analysis(self, response):
        if response['status'] == 'success':
            mood = response['photos'][0]['tags'][0]['attributes']['mood']
            query = "INSERT INTO picture (mood, confidence) VALUES ('{0}',{1})".format(mood['value'], mood['confidence'])
            return self.safe_execute(query)
        return False
    
    def save_text_analysis(self,response):
        if response['status'] == 'success':
            mood = response['photos'][0]['tags'][0]['attributes']['mood']
            query = "INSERT INTO picture (mood, confidence) VALUES ('{0}',{1})".format(mood['value'], mood['confidence'])
            return self.safe_execute(query)
        return False

    def safe_execute(self,query):
        try:
            print "attempting to execute query; {0}..".format(query)
            cursor.execute(query)
            return True
        except:
            return False
