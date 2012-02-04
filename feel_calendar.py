from feel_base import BaseHandler
import datetime

class CalendarHandler(BaseHandler):
    
    fields = ['startTime','endTime','allDay','location','title','attendees','reminder','lengthMinutes','details']
    incoming_time_format = "%a %b %d %H:%M:%S %Z %Y"
    server_time_format = "%Y-%m-%d %H:%M:%S"
    
    def post(self):
        self.write("posted event!")
        
        args = dict()
        for field in self.fields:
            try:
                args[field] = self.request.arguments[field][0]
                if args[field] == '':   # in case http post includes field name but there is no info. subject to change
                    args[field] = None
            except KeyError:
                args[field] = None
                print "could not find the field {0} just set to None".format(field)
                
        if args['startTime'] and args['endTime']:
            # convert to python datetime to manipulate easily
            start_time = datetime.datetime.strptime(args['startTime'], self.incoming_time_format)
            end_time = datetime.datetime.strptime(args['startTime'], self.incoming_time_format)
            # not create strings in the format of server
            start_time_string = start_time.strftime(self.server_time_format)
            end_time_string = end_time.strftime(self.server_time_format)
            # now revise args that will be saved in database
            args['startTime'] = start_time_string
            args['endTime'] = end_time_string
            args['timeZone'] = start_time.strftime("%z")
            
        elif  args['reminder']:   # if there is no start&end times, then it is a reminder
            reminder= datetime.datetime.strptime(args['reminder'], self.incoming_time_format)
            reminder_string = reminder.strftime(self.server_time_format)
            args['reminder'] = reminder_string
            args['timeZone'] = reminder.strftime("%z")
        else:
            print "will try to save, but error in timestamps"

        self.save_calendar_data(args)
        
    def get(self):
        self.write("calendar handler!")
        