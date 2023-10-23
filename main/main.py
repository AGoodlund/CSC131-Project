from flask import Flask, request, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

PORT = 5973
HOST = "127.0.0.1"


#The following are imported from my old code and will not be needed later- Sheridan
#TODO Decide if you need to delete -SL
"""user_data = [
    {"id": 1, "name": "Sheridan Lynch", "type": "student", "schedule_id": 26}, #26 = 1A in hex and I didn't want to keep this as a string -Sl

]

JOBS = [
    {"id": 1, "name": "Sheridan Lynch", "type": "student", "schedule_id": 26}, #26 = 1A in hex and I didn't want to keep this as a string -Sl

] #Cloned for practice. Please delete jobs and replace with user_data. -SL

schedule_data = [
    {"schedule_id": "1A", "user_id": "1", "preferred_time": "Monday: 2pm-5pm"}
] """

 
# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'maindb'

mysql = MySQL(app)


#TODO Decide if needed -SL
def _find_next_id(data_list):
    """Small helper function to find the next ID from a previous list of data"""
    max_id = 0
    for data in data_list:
        if data["id"] > max_id:
            max_id = data["id"]

    # Calculate the next ID
    next_id = max_id + 1
    return next_id


## TESTS 

@app.get("/test")
def hello_world():
    return ("Hello World")


@app.get("/")
def welcome():
    return render_template('home.html')



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
    
    return render_template('phrase.html', data=phrases)


#Please remove everything related to 'jobs' in the future -SL
#TODO Change everything

"""
@app.route("/users/test", methods=["GET"])
def job_test():
    return render_template('home.html', jobs = JOBS)

@app.route("/api/users", methods=["GET"])
def user_out():
    return jsonify(JOBS) """ 



"""

@app.route("/users/<int:user_id>", methods=["GET"])
def get_single_user_data(user_id):
    found_user = None
    for user in user_data:
        if user['id'] == user_id:
            found_user = user
            break
    if found_user is None:
        return {"ERROR": f"No Data Found for ID {user_id}"}, 404
    
    return jsonify(found_user)


#POST

@app.route("/users", methods=["POST"])
def add_user_data():
    if request.is_json:
        response = request.get_json()
        response["id"] = _find_next_id(user_data)
        user_data.append(response)
        return jsonify(response), 201
    return {"ERROR. Request must be in JSON :("}, 415



@app.route("/users/<int:user_id>", methods=["PUT"])
def edit_user_data(user_id):
    for user in user_data:
        if user["id"] == user_id:
            if request.is_json:
                if 'name' in request.json or 'type' in request.json:
                    user['name'] = request.json.get('name', user['name']) 
                    user['type'] = request.json.get('type', user['type'])
                    return jsonify(user), 200
                else:
                    return ("ERROR: Bad request. Missing required user fields :("), 400
            return {"ERROR. Request must be in JSON :("}, 415
    return {"ERROR" : f"No data found for user ID {user_id}"}, 404

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user_data(user_id):
    for user in user_data:
        if user["id"] == user_id:
         user_data.remove(user)
         return ("User Successfully Deleted")

    return {"ERROR" : f"No data found for user ID {user_id}. Action was unsuccessful."}, 404

"""



    
if __name__ == '__main__':
  app.run(host=HOST, port=PORT)