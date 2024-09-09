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

collection = db['test2']


collection2 = db['test3']


UPLOAD_FOLDER = 'uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


if not os.path.exists(UPLOAD_FOLDER):

    os.makedirs(UPLOAD_FOLDER)


@app.route("/")

def hello():

    name = collection.find_one({'id': '1234'})

    return render_template('login.html', member_no='8712899908', crn_no='0111-2839', dob='22-08-2006', name=name)


@app.route('/get_user_data', methods=['GET'])

def get_user_data():

    user_id = request.args.get('id')

    user = collection2.find_one({"id": "1234"})

    if user:

        image_base64 = base64.b64encode(user['screenshot']).decode('utf-8') if 'screenshot' in user else None

        return jsonify({

            'name': user.get('name'),

            'image': image_base64

        }), 200

    else:

        return jsonify({'error': 'User not found'}), 404


@app.route('/update_user2', methods=['POST'])

def update_user2():

    data = request.form

    user_id = data.get('id')
    bid=data.get('bid')

    new_data = collection2.find_one({"id": user_id,"bid":bid})
    if new_data==None:
        collection2.insert_one({'id':data.get('id'),'pass':data.get('id'),'bid':bid})
    new_data = collection2.find_one({"id":user_id})

   

    if data.get('acc_no')!='':

        new_data['acc_no']=data.get('acc_no')

    if data.get('ifsc')!='':

        new_data['ifsc']=data.get('email')

    if data.get('bank_name')!='':

        new_data['bank_name']=data.get('bank_name')
        

  
    new_data['deal_type']='bajaj'
    if 'image' in request.files:

        image = request.files['image']

        if image:

            filename = secure_filename(image.filename)

            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            image.save(filepath)

            with open(filepath, 'rb') as file:

                binary_data = file.read()

            new_data['image'] = binary_data


    result = collection2.update_one({'id': user_id}, {'$set': new_data})

    if result.matched_count == 0:

        return jsonify({'error': 'User not found'}), 404

    return jsonify({'success': 'User updated successfully'}), 200
@app.route('/update_user', methods=['POST'])

def update_user():

    data = request.form

    user_id = data.get('id')
    bid=data.get('bid')

    new_data = collection.find_one({"id": user_id,"bid":bid})
    if new_data==None:
        collection.insert_one({'id':data.get('id'),'pass':data.get('id'),'bid':bid})
    new_data = collection.find_one({"id":user_id})

    if data.get('name')!='':
        new_data['name']=data.get('name')

    if data.get('acc_no')!='':

        new_data['acc_no']=data.get('acc_no')

    if data.get('ifsc')!='':

        new_data['ifsc']=data.get('ifsc')

    if data.get('bank_name')!='':

        new_data['bank_name']=data.get('bank_name')
        

    if data.get('loan_amount')!='':

        new_data['loan_amount']=data.get('loan_amount')

    if data.get('loan_type')!='':

        new_data['loan_type']=data.get('loan_type')

    if data.get('address')!='':

        new_data['address']=data.get('address')

    if data.get('field')!='':

        new_data['field']=data.get('field')

    if data.get('date')!='':

        new_data['date']=data.get('date')

    if data.get('intrest')!='':

        new_data['intrest']=data.get('intrest')

    if data.get('emi')!='':

        new_data['emi']=data.get('emi')
    if data.get('status')!='':
        new_data['status']=data.get('status')
    if data.get('dob')!='':

        new_data['dob']=data.get('dob')
    if data.get('charge')!='':
        new_data['charge']=data.get('charge')

    if data.get('charge_amount')!='':
        new_data['charge_amount']=data.get('charge_amount')
    if data.get('year')!='':
        new_data['year']=data.get('year')
    if data.get('month')!='':
        new_data['month']=data.get('month')

    new_data['deal_type']='bajaj'
    if 'image' in request.files:

        image = request.files['image']

        if image:

            filename = secure_filename(image.filename)

            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            image.save(filepath)

            with open(filepath, 'rb') as file:

                binary_data = file.read()

            new_data['image'] = binary_data


    result = collection.update_one({'id': user_id}, {'$set': new_data})

    if result.matched_count == 0:

        return jsonify({'error': 'User not found'}), 404



    return jsonify({'success': 'User updated successfully'}), 200

@app.route("/login", methods=["GET", "POST"])

def login():

    name = collection.find_one({'id': request.form['id'],'bid':request.form['bid']})

    if name:

        if name['deal_type'] == 'bajaj':

            loan_status_color = 'rgb(255, 0, 0)'

            logo = "https://th.bing.com/th/id/OIP.YR3v1Mo5KacvGQMMxFNLsAAAAA?w=250&h=90&rs=1&pid=ImgDetMain"

            nav_color = '#0671B9'

            list_head = 'rgb(45, 45, 255)'

            tr_even = 'rgb(164, 164, 255)'

        else:

            logo = "https://chandanvarshney.in/wp-content/uploads/2020/06/mudra-logo.png"

            loan_status_color = 'rgb(0, 0, 255)'

            nav_color = '#f3b27d'

            list_head = '#ca631f'

            tr_even = '#ecc3a8'

        return render_template('index.html', tr_even=tr_even, list_head=list_head, nav_color=nav_color, logo=logo, loan_status_color=loan_status_color, member_no='8712899908', crn_no='0111-2839', dob='2-08-2006', name=name)

    else:

        return render_template('error.html', member_no='8712899908', crn_no='0111-2839', dob='22-08-2006', name=name)


@app.route("/pay", methods=["GET", "POST"])

def pay():

    name2 = collection2.find_one({'id': request.form['bid']})

    name = collection.find_one({'id': request.form['id']})


    return render_template('payment.html', name=name, name2=name2)


@app.route('/image/<image_id>')

def get_image(image_id):

    image_data = collection2.find_one({'id': image_id})

    if image_data:

        return send_file(BytesIO(image_data['image']), mimetype='image/jpg')

    else:

        return 'Image not found', 404


@app.route("/confirm_payment", methods=["POST"])

def confirm_payment():

    name = collection.find_one({'id': request.form['id']})

    if name:

        if name['deal_type'] == 'bajaj':

            loan_status_color = 'rgb(255, 0, 0)'

            logo = "https://th.bing.com/th/id/OIP.YR3v1Mo5KacvGQMMxFNLsAAAAA?w=250&h=90&rs=1&pid=ImgDetMain"

            nav_color = '#0671B9'

            list_head = 'rgb(45, 45, 255)'

            tr_even = 'rgb(164, 164, 255)'

        else:

            logo = "https://chandanvarshney.in/wp-content/uploads/2020/06/mudra-logo.png"

            loan_status_color = 'rgb(0, 0, 255)'

            nav_color = '#f3b27d'

            list_head = '#ca631f'

            tr_even = '#ecc3a8'



    name3 = collection.find_one({'id':'1234'})

    name2 = request.form['name']

    email = request.form['email']

    amount = request.form['amount']

    screenshot = request.files['screenshot']


    if screenshot:

        filename = secure_filename(screenshot.filename)

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        screenshot.save(filepath)


        with open(filepath, 'rb') as file:

            binary_data = file.read()



        collection2.insert_one({

            'name': name2,

            'email': email,

            'amount': amount,

            'screenshot': binary_data

        })


        flash('Payment confirmed successfully!', 'success')

        return render_template('index.html', tr_even=tr_even, list_head=list_head, nav_color=nav_color, logo=logo, loan_status_color=loan_status_color, member_no='8712899908', crn_no='0111-2839', dob='2-08-2006', name=name)

    else:

        flash('Failed to confirm payment. Please try again.', 'error')

        return redirect('/pay')


