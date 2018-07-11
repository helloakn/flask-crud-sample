from flask import Flask, render_template, Blueprint
#from sample_page import sample_page
from admin.admin import admin
from flaskext.mysql import MySQL
mysql = MySQL()

app = Flask(__name__)
app.register_blueprint(admin) 
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)                 

@app.route('/')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True)
   