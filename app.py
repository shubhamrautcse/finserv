from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file


from flask_pymongo import PyMongo


from werkzeug.utils import secure_filename

import urllib.parse

import os


from io import BytesIO

from flask import Flask, render_template, request, redirect, url_for, flash,session,send_file

from flask_pymongo import PyMongo

from pymongo import MongoClient

from bson.objectid import ObjectId

from werkzeug.utils import secure_filename

import os

from io import BytesIO

from flask import Flask, request, jsonify

from pymongo import MongoClient

import base64

import base64



app = Flask(__name__)


app.secret_key = 'your_secret_key'



# MongoDB Atlas connection string


username = urllib.parse.quote_plus('sftghsffth')

password = urllib.parse.quote_plus('giHkXMkhFVwBdfLb')

# Initialize MongoDB collections MongoDB Atlas connection string


app.config["MONGO_URI"] = f"mongodb+srv://{username}:{password}@cluster0.m8r2cjv.mongodb.net/dbname?retryWrites=true&w=majority"

mongo = PyMongo(app)

db = mongo.db

collection = db['user4']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emicard')
def emicard():
    return render_template('emicard.html')
@app.route('/loan')
def mai():
    return render_template('main.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/submit' ,methods=["GET", "POST"])
def submited():
    collection.insert_one({'name':request.form.get('name'),'email':request.form.get('email'),'dob':request.form.get('dob'),'Loantype':request.form.get('Loantype'),'amount':request.form.get('amount'),'number':request.form.get('number'),'year':request.form.get('year'),'month':request.form.get('month')})
    return render_template('submited.html')

@app.route('/loan_status')
def loan_status():
    name = collection.find_one({'id': request.form['id'],'bid':request.form['bid']})
    return render_template('loan_status.html',name=name)


if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0')
