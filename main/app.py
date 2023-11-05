import os
import json
from flask import Flask, render_template, request, url_for, redirect, jsonify
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
  days = db.relationship('Day', backref='week')

  def __repr__(self):
    return f'<Week "{self.month_id}">'



class Day(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  day = db.Column(db.String(100), nullable=False)
  week_id = db.Column(db.Integer, db.ForeignKey('week.id'))
  times = db.relationship('Time', backref='day')

  def __repr__(self):
    return f'<Day "{self.week_id}">'


class Time(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  time = db.Column(db.String(100))
  day_id = db.Column(db.Integer, db.ForeignKey('day.id'))

  def __repr__(self):
    return f'<Time "{self.day_id}">'
    

# Home and other pages
@app.get("/")
def welcome():
    return render_template('home.html')


@app.route("/buttons", methods=["GET"])
def get_buttons():
  
  return render_template('timeSlots.html')


# GET

#Gets the web version of months
@app.route('/months')
def index():
  months = Month.query.all()
  return render_template('index.html', months=months)


# Show Day of specific Week and show Times in Day
@app.route('/day/<int:day_id>/', methods=('GET', 'POST'))
def display_day(day_id):
  day = Day.query.get_or_404(day_id)
  # Add Times to specific Day
  if request.method == 'POST':
    time = Time(time=request.form['time'], day=day)
    db.session.add(time)
    db.session.commit()
    return redirect(url_for('display_day', day_id=day.id))
    
  return render_template('day.html', day=day)




# Delete a Time in specific Day
@app.post('/times/<int:time_id>/delete')
def delete_time(time_id):
  time = Time.query.get_or_404(time_id)
  day_id = time.day.id
  db.session.delete(time)
  db.session.commit()
  return redirect(url_for('display_day', day_id=day_id))


# Update a Time in a specific Day
@app.post('/times/<int:time_id>/edit')
def edit_time(time_id): 
  update_time = Time.query.get_or_404(time_id)
  day_id = update_time.day.id 
  time = request.form['time']
  update_time.time = time 
  db.session.add(update_time)
  db.session.commit()
  return redirect(url_for('display_day', day_id=day_id))




if __name__ == '__main__':
  app.run() 