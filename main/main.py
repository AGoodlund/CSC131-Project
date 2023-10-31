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
@app.route('/months', methods =["GET"])
def index():
  months = Month.query.all()
  return render_template('index.html', months=months)

#Gets the JSON version of months
#Gives the 'not json serialized' error.
""" @app.route('/api/months', methods =["GET"])
def get_months_json():
  months = Month.query.all()
  return jsonify(months) """

#Gets the JSON version of phrases
"""@app.route("/api/phrases", methods=["GET"])
def get_phrases_json():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM test")
    phrases = cursor.fetchall()
    cursor.close()
    return jsonify(phrases)"""




if __name__ == '__main__':
  app.run() 







"""
from flask_mysqldb import MySQL

app = Flask(__name__)

PORT = 5973
HOST = "127.0.0.1"
 
# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'maindb'

mysql = MySQL(app)





## TESTS 

@app.get("/api/test")
def hello_world():
    return ("Hello World")


# BONUS! Gets JSON if it contains a phrase
# I figured out how to do it and have a feeling it will be needed later -SL
# It's not the best but it's almost perfect so I'm keeping it. 
# We may want to use 'CONTAINS() instead for practical reasons -SL
@app.route("/api/test/phrases/<string:querry>", methods=["GET"])
def get_phrases_from_string(querry):
    phrases = None

    cursor = mysql.connection.cursor()

    find = "SELECT * FROM test WHERE phrase LIKE %s"
    cursor.execute(find,querry)
    phrases = cursor.fetchall()
    cursor.close()

    if phrases is None:
        return {"ERROR": f"No Data Found containing the phrase {querry}"}, 404
    
    return jsonify(phrases)


# GET

#Gets the JSON version of phrases
@app.route("/api/phrases", methods=["GET"])
def get_phrases_json():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM test")
    phrases = cursor.fetchall()
    cursor.close()
    return jsonify(phrases)


#Gets the user webpage for phrases
@app.route("/phrases", methods = ["GET"])
def display_phrases():
  cursor = mysql.connection.cursor()
  cursor.execute("SELECT * FROM test")
  data = cursor.fetchall()
  cursor.close()
  return render_template('phrase.html', data=data)


#Gets the JSON version of one phrase
@app.route("/api/phrases/<string:phrase_id>", methods=["GET"])
def get_phrases_json_single(phrase_id):
    phrases = None

    cursor = mysql.connection.cursor()

    find = "SELECT * FROM test WHERE id = %s"
    cursor.execute(find,phrase_id)
    phrases = cursor.fetchall()
    cursor.close()

    if phrases is None:
        return {"ERROR": f"No Data Found for ID {phrase_id}"}, 404
    
    return jsonify(phrases)


#Gets the user webpage for one phrase

@app.route("/phrases/<string:phrase_id>", methods=["GET"])
def display_phrases_single(phrase_id):
    phrases = None

    cursor = mysql.connection.cursor()

    find = "SELECT * FROM test WHERE id = %s"
    cursor.execute(find,phrase_id)
    phrases = cursor.fetchall()
    cursor.close()

    if phrases is None:
        return {"ERROR": f"No Data Found for ID {phrase_id}"}, 404
    
    return render_template('phrase.html', data=phrases)"""



#TODO Add the rest of CRUD functionality

#THIS STUFF WAS COMMENTED OUT

#POST

"""@app.route("/api/phrases", methods=["POST"])
def add_phrase_data():
    if request.is_json:
        response = request.get_json()
        #get_id = "LAST_VALUE"
        insert = "INSERT INTO EMPLOYEE(id, phrase) VALUES (%s, %s,)"
        #next_id = 
        data = (420,response)
        cursor = mysql.connection.cursor()

        cursor.execute(insert,data)
        cursor.commit()

        cursor.close()
        return jsonify(response), 201
    return {"ERROR. Request must be in JSON :("}, 415"""

"""


#POST

@app.route("/phrases", methods=["POST"])
def add_phrase_data():
    if request.is_json:
        response = request.get_json()
        response["id"] = _find_next_id(phrase_data)
        user_data.append(response)
        return jsonify(response), 201
    return {"ERROR. Request must be in JSON :("}, 415



@app.route("/phrases/<int:phrase_id>", methods=["PUT"])
def edit_phrase_data(phrase_id):
    for phrase in phrases:
        if phrase["id"] == phrsae_id:
            if request.is_json:
                if 'name' in request.json or 'type' in request.json:
                    phrase['name'] = request.json.get('name', phrase['name']) 
                    phrase['type'] = request.json.get('type', phrase['type'])
                    return jsonify(phrase), 200
                else:
                    return ("ERROR: Bad request. Missing required phrase fields :("), 400
            return {"ERROR. Request must be in JSON :("}, 415
    return {"ERROR" : f"No data found for phrase ID {phrase_id}"}, 404

@app.route("/phrases/<int:phrase_id>", methods=["DELETE"])
def delete_phrase_data(phrase_id):
    for phrase in phrase_data:
        if phrase["id"] == phrase_id:
         phrase_data.remove(phrase))
         return ("Phrase Successfully Deleted")

    return {"ERROR" : f"No data found for phrase ID {phrase_id}. Action was unsuccessful."}, 404

"""



    
"""if __name__ == '__main__':
  app.run(host=HOST, port=PORT)"""