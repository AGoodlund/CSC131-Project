import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func 

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




class Month(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  month = db.Column(db.String(100), nullable=False)
  weeks = db.relationship('Week', backref='month')
  
  def __repr__(self):
    return f'<Month "{self.month}">'



class Week(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  month_id = db.Column(db.Integer, db.ForeignKey('month.id'))

  def __repr__(self):
    return f'<Week "{self.month_id}">'



class Day(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  day = db.Column(db.String(100), nullable=False)
  week_id = db.Column(db.Integer, db.ForeignKey('week.id'))

  def __repr__(self):
    return f'<Day "{self.week_id}">'


class Time(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  time = db.Column(db.String(100))
  day_id = db.Column(db.Integer, db.ForeignKey('day.id'))

  def __repr__(self):
    return f'<Time "{self.day_id}">'
    





  





"""
@app.route('/')
def index():
  months = Month.query.all()
  return render_template('index.html', months=months)
"""


if __name__ == '__main__':
  app.run() 