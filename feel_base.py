from feel_database import Database as db
import tornado.web
cursor = db.cursor

class BaseHandler(tornado.web.RequestHandler):

    def get_current_user_key(self):
        return self.get_secure_cookie("key")

    def get_current_user_email(self):
        key = self.get_current_user_key()
        if key:
            query = "SELECT * FROM login WHERE `key`='{}' LIMIT 1".format(key)
            if self.safe_execute(query):
                result = cursor.fetchone()
                return result[0]
        
        
    def is_user_logged_in(self):
        key = self.get_current_user_key()
        if key:
            query = "SELECT * FROM login WHERE `key`='{}' LIMIT 1".format(key)
            if self.safe_execute(query):
                result = cursor.fetchone()
                return (result!=None)

        return False
       
    def is_correct_login(self, email, password):
        print "checking if correct login"
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
        query = "DELETE FROM login WHERE `key`='{}'".format(self.get_current_user_key())
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
            email = self.get_current_user_email()
            query = "INSERT INTO picture (email, mood, confidence) VALUES ('{0}','{1}',{2})".format(email, mood['value'], mood['confidence'])
            return self.safe_execute(query)
        return False
    
    # TODO: pass other email fields into text analysis.
    def save_text_analysis(self,response):
        sentiment = response['docSentiment']['type']
        score = response['docSentiment']['score']
        text = response['text']
        email = self.get_current_user_email()
        query = "INSERT INTO text (email , text, sentiment, score) VALUES ('{0}','{1}','{2}',{3})".format(email, text, sentiment, score )
        return self.safe_execute(query)
    
    def save_eda_data(self, start_time_string, end_time_string, time_zone, eda, temperature, acc_x, acc_y, acc_z):
        email = self.get_current_user_email()
        query = "INSERT INTO eda (email, start_time, end_time, time_zone, eda, temperature, acc_x, acc_y, acc_z) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(email,start_time_string, end_time_string, time_zone, eda, temperature, acc_x, acc_y, acc_z)
        return self.safe_execute(query)
    
    def save_calendar_data(self, args):
        email = self.get_current_user_email()
        query = """INSERT INTO calendar (email,start_time,end_time,time_zone,all_day,location,title,attendees,reminder,length_minutes,details"
                VALUES ('{0}','{1}','{2}','{3}',{4},'{5}','{6}','{7}','{8}',{9},'{10}')""".format(email, args['startTime'], args['endTime'], args['timeZone'], args['allDay'], args['location'], args['title'],args['attendees'],args['reminder'],args['lengthMinutes'],args['details'])
        return self.safe_execute(query)
        
    def safe_execute(self,query):
        try:
            print "attempting to execute query; {0}..".format(query)
            cursor.execute(query)
            return True
        except Exception as ex:
            print "error executing the query; {0}".format(query)
            print type(ex)
            print ex.args
            return False
