import pymysql

class Database(object):
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='demo')
        conn.autocommit(1)
        cursor = conn.cursor()

    
