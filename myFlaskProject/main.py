from flask import Flask, request, render_template, jsonify
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


@app.route("/phrases", methods = ["GET"])
def display():
  cursor = mysql.connection.cursor()
  cursor.execute("SELECT * FROM test")
  data = cursor.fetchall()
  cursor.close()
  return render_template('phrase.html', data=data)



    
if __name__ == '__main__':
  app.run(host=HOST, port=PORT)