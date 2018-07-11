from flask import Flask
from flaskext.mysql import MySQL
class dbConnect:
    app = Flask(__name__)
    mysql = MySQL()
    tmp = 1
    def __init__(self):
        #self.app = app
        self.tmp = 1
        self.app.config['MYSQL_DATABASE_USER'] = 'root'
        self.app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
        self.app.config['MYSQL_DATABASE_DB'] = 'EmpData'
        self.app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        self.mysql.init_app(app)
    def akn(self):
        self.tmp += self.tmp
        
        return "aa"+str(self.tmp)