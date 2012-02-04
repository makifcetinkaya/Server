from feel_base import BaseHandler
from edatoolkit import qLogFile
import datetime

class EDAHandler(BaseHandler):
    SLICE_LENGTH = datetime.timedelta(minutes = 30) #length of eda slices in minutes
    def get(self):
        self.write('eda handler!')
        self.test_eda()
    def post(self):
        
        if self.is_user_logged_in():
            uploaded_file =  self.request.files.get("eda")[0]
            file_name = self.get_current_user_email().partition('.')[0]+"-eda-"+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            output_file = open("uploads/eda/" + file_name, 'w' )
            output_file.write(uploaded_file['body'])
            self.finish("file has been uploaded")
        else:
            print "user is not logged in"
            self.redirect("/login")
            
    def test_eda(self):
        eda_file = qLogFile("uploads/eda/eda")
        slice_start_time = eda_file.startTime #datetime.datetime object
        end_time = eda_file.endTime
        while slice_start_time<end_time:
            slice_end_time = slice_start_time+self.SLICE_LENGTH if (slice_start_time+self.SLICE_LENGTH < end_time) else end_time
            
            slice = eda_file.qLogFileSlice(slice_start_time,slice_end_time)
            
            eda = ",".join(str(x) for x in slice[0])
            temperature =",".join(str(x) for x in slice[1])
            acc_x = ",".join(str(x) for x in slice[2])
            acc_y = ",".join(str(x) for x in slice[3])
            acc_z = ",".join(str(x) for x in slice[4])
            
            start_time_string = slice_start_time.strftime("%Y-%m-%d %H:%M:%S")
            end_time_string = slice_end_time.strftime("%Y-%m-%d %H:%M:%S")
            
            timezone = slice_start_time.strftime("%z")
            
            self.save_eda_data(start_time_string, end_time_string, timezone, eda, temperature, acc_x, acc_y, acc_z)
            
            slice_start_time = slice_start_time+self.SLICE_LENGTH
        
       # print "|".join(str(x) for x in eda_file.EDA())
                                                      
            