import os                          
from os.path import join,  dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(_file_),'.venv')
load_dotenv(dotenv_path)

MONGODB_URI =os.environ.get("MONGODB_URI")
DB_NAME=os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db =client[DB_NAME]
app = Flask(_name_)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive=request.form['address_give']
    size_receive=request.form['size_give']
    doc={
        'name':name_receive,
        'address':address_receive,
        'size':size_receive,
    }
    db.orders.insert_one(doc)
    return jsonify({'msg': 'Complete'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    order_list =list(db.orders.find({},{'_id':False}))
    return jsonify({'orders': order_list})

if _name_ == '_main_':
    app.run('0.0.0.0', port=5000, debug=True)