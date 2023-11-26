import os
import json
import Event_class #This is Aaron's file
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin, LoginManager, login_user, current_user, login_required, logout_user 

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysupersecretkey'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

user_time = db.Table('user_time',
                    db.Column('time_id', db.Integer, db.ForeignKey('time.id')),
                     db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                    )


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  name = db.Column(db.String(100))
  schedule = db.relationship('Time', secondary=user_time, backref='times')

  def __repr__(self):
    return f'<User "{self.name}">'




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



#API

@app.route('/api')
def eventView():
  return Event_class.viewEvents()

@app.route('/api/test')
def eventTest():
  Event_class.test()
  out = "Test Complete: SEE CONSOLE"
  return out
    


@app.route('/api/day/<int:day_id>/', methods=('GET', 'POST'))
def arrayDay (day_id):
  day = Day.query.get_or_404(day_id)
  print("Get works.")
  # Add Times to specific Day
  if request.method == 'POST':
    print("Post works.")
    #time = Time(time=request.form['time'], day=day) #Needs to be updated to handle an array -SL
    # THE ABOVE NEEDS TO BE DONE SEVERAL TIMES

    timeArray = request.form['postOutput']
    #db.session.add(time)
    #db.session.commit()
    return redirect(url_for('display_day', day_id=day.id))
    
  return render_template('calendar.html', day=day)

#This is where I'm experimenting with uploading the time array -Sl





# Home and other pages
@app.get("/")
def welcome():
    return render_template('home.html')


@app.route("/times", methods=["GET"])
def get_buttons():
  return render_template('timeSlots.html')

@app.route("/calendar", methods=["GET"])
def get_calendar():
  return render_template('calendar.html')

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


#EVENT FUNCTION

@app.route('/profile')
@login_required
def profile():
  return render_template('profile.html', name=current_user.name) 

@app.route('/login', methods=('GET', 'POST'))
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
      flash('Please check your login details and try again.')
      return redirect(url_for('login'))

    login_user(user, remember=remember)
    return redirect(url_for('profile'))
    
  return render_template('login.html')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
  if request.method == 'POST':
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
      flash('Email address already exists!')
      return redirect(url_for('signup'))

    new_user = User(email=email, password=generate_password_hash(password, method='scrypt'), name=name)

    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))
    
  return render_template('signup.html')


@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('welcome'))


# Months page
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
    time = Time(time=request.form['time'], day=day) #Needs to be updated to handle an array -SL
    db.session.add(time)
    db.session.commit()
    return redirect(url_for('display_day', day_id=day.id))
    
  return render_template('calendar.html', day=day)


# Delete a Time in specific Day
@app.post('/times/<int:time_id>/delete')
def delete_time(time_id):
  time = Time.query.get_or_404(time_id)
  day_id = time.day.id
  db.session.delete(time)
  db.session.commit()
  return redirect(url_for('display_day', day_id=day_id))


# Update a Time in a specific Day
@app.put('/times/<int:time_id>/edit')
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