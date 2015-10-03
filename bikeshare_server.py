import sqlite3
from flask import Flask, render_template, request
from contextlib import closing
#from flaskr import init_db

app = Flask(__name__)
app.config.from_object(__name__)

#DATABASE = '/tutorial.db'
#
#def connect_db():
#    return sqlite3.connect(app.config['DATABASE'])
#    
#def init_db():
#    with closing(connect_db()) as db:
#        with app.open_resource('schema.sql', mode='r') as f:
#            db.cursor().executescript(f.read())
#        db.commit()
#
#@app.before_request
#def before_request():
#    Flask.db = connect_db()
#    
#@app.teardown_request
#def teardown_request(exception):
#    db = getattr(Flask, 'db', None)
#    if db is not None:
#        db.close()
#        
#@app.route('/')
#def show_entries():
#    cur = Flask.db.execute('select title, text from entries orer by id desc')
#    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
#    return render_template('show_entries.html', entries=entries)

@app.route('/login', methods=['POST', 'GET'])
def login():
    print(request)
    error = None
    if request.method == 'POST':
        if valid_login(request.form['bikecode']):
            return render_template('checkout.html')
        else:
            error = 'Invalid code'
    return render_template('login.html', error=error)
    
@app.route('/checkout', methods=['POST', 'GET'])
def check_out():
    print(request)
    error = None
    if request.method == 'POST':
        if valid_id(request.form['userid']):
            return render_template('thankyou.html')
        else:
            error = 'Invalid user id'
    return render_template('checkout.html', error=error)
    
def valid_login(bikecode):
    return True
    
def valid_id(userid):
    return True

@app.route('/login')
def index():
    return render_template('login.html')
    
if __name__ == '__main__':
    app.run()