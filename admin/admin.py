from flask import Blueprint,render_template,session,redirect,url_for,request
import sys
#from config.dbConnect import dbConnect
#from config.db import db


admin = Blueprint('admin', __name__, 
template_folder='templates',
static_folder='static')

def Authenticate(req):
    username = req.get('user')
    password = req.get('password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

@admin.route('/admin/login',methods = [ 'GET'])
def login():
    #bdConnect.akn()
    #return ''.join(sys.path)
    #db = dbConnect()
    #db.akn()
    #db.akn()
    #db.akn()
    #tmpp = 'the values is'+str(db.tmp)
    #return 'the values is'+str(db.akn())
    return render_template('login.html') 

@admin.route('/admin/login',methods = [ 'POST'])
def loginPost():
    if request.method == 'POST':
        result = request.form
        tmp = ""
        
        Authenticate(result)
        for key, value in result.items():
            tmp += ''.join((key,value))
        return tmp
    return render_template('login.html',result = result) 

@admin.route('/admin')
def index():
   if 'username' in session:
        username = session['username']
        return username
   return redirect(url_for('admin.login'))



#@admin.route('/admin')
#def index():
#    return render_template('login.html')