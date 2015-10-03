from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tutorial.db'
db = SQLAlchemy(app)

class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checked_out = db.Column(db.DateTime(), unique=True)
    checked_in = db.Column(db.DateTime(), unique=True)
    home_loc = db.Column(db.String(), unique=True)
    in_out = db.Column(db.Boolean(), unique=True)
    
    def __init__(self, checked_out, checked_in, home_loc, in_out):
        self.checked_out = checked_out
        self.checked_in = checked_in
        self.home_loc = home_loc
        self.in_out = in_out
        
    def __repr__(self):
        return (str(self.id) + ', ' + str(self.checked_out) + ', ' + str(self.checked_in) + ', ' + 
            self.home_loc + ',' + str(self.in_out))