from flask import render_template, request, jsonify
from server import app
from database.db import connectionSQL, insert_records, consult_records

@app.route('/')
def home_page():
    connectionSQL()
    return render_template("home.html")

@app.route('/register')
def register_page():
    return render_template("register.html")
    
@app.route('/consult')
def consult_page():
    return render_template("consult.html")
    
@app.route('/register_user_db', methods=['post'])
def register_user_db():
    data_user = request.form
    id = data_user["id"]
    name = data_user["name"]
    lastname = data_user["lastname"]
    birthday = data_user["birthday"]
    insert_records(id,name,lastname,birthday)
    return render_template("register.html")
    
@app.route('/consult_user_db', methods=['post'])
def consult_user_db():
    data_id = request.get_json()
    result = consult_records(data_id["id"])
    if result != None and len(result) > 0:
        name = result[0][1]
        lastname = result[0][2]
        birthday = result[0][3]
        resp_data = {"status":"OK",
            "name": name,
            "lastname": lastname,
            "birthday": birthday
        }
    else:
        resp_data = {"status":"Error"}
    print (result)
    print(resp_data)
    return jsonify(resp_data)
    