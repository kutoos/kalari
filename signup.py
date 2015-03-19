from flask import Flask,redirect,request
from flask import render_template
from flask import send_file, send_from_directory
from flask import make_response
from flask import g

import uuid
import sqlite3

app = Flask(__name__)

DATABASE = 'user.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()
    g.c = g.db.cursor()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.commit()
        g.db.close()

def check_user_exists(email):
    e = (email,)
    g.c.execute('''SELECT email FROM user WHERE email=?''',e)
    if g.c.fetchone():
        return True
    return False

@app.route('/signup',methods=['POST'])
def signup():
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']
    if not check_user_exists(email):
        # Insert the user here. 
        user_details=[(name,email,password),]
        g.c.executemany('INSERT INTO user VALUES (?,?,?)', user_details)
    return redirect('/')

@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    if not request.cookies.has_key('sid'):
        response.set_cookie('sid',str(uuid.uuid1()),max_age=3600)
    return response

if __name__ == '__main__':
    app.run(debug = True)
