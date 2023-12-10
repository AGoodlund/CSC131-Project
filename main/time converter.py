import os

from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysupersecretkey'
db = SQLAlchemy(app)

class time_finder:
    
    time_list = Time(time=request.form['timeSubmission'], day=day)
    
    def create_open_times_list():
        for time in time_finder.time_list:
            if time["value"] is '1':
                db.session.add(time['value'])
        db.session.commit()

#I think this goes somewhere between lines 177 and 188 in app.py