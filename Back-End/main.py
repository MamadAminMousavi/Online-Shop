from flask import Flask, jsonify , request
import sqlite3
from flask_cors import CORS, cross_origin
import io
from datetime import datetime
from fileinput import filename 

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect('./Online-shop.db')
    conn.row_factory = sqlite3.Row
    return conn

# back test
@app.route('/',methods=['GET'])
def test():
    return "ok"

#-------------------------------------------------


# users crud function
def get_all_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Users')
    customers = cur.fetchall()
    final_customers = []
    for customer in customers:
        final_customers.append({
            "user_id": customer[0],
            "username": customer[1],
            "password_hash": customer[2],
            "email": customer[3],
            "phone_number": customer[4],
            "registration_date": customer[5],
            "role": customer[6],
            "default_shipping_address": customer[7],
        })
    conn.close()
    return final_customers

def get_users(users_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Users WHERE user_id = ?', (users_id,))
    User = cur.fetchone()
    final_users = {
            "user_id": User[0],
            "username": User[1],
            "password_hash": User[2],
            "email": User[3],
            "phone_number": User[4],
            "registration_date": User[5],
            "role": User[6],
            "default_shipping_address": User[7]
        }
    conn.close()
    return final_users
def create_user(username, password_hash,email,phone_number, role,default_shipping_address):
    conn = get_db_connection()
    cur = conn.cursor()
    registration_date = datetime.today().strftime('%Y-%m-%d')
    cur.execute('INSERT INTO Users (username, password_hash,email,phone_number,registration_date,role,default_shipping_address) VALUES (?, ?, ?, ? , ?, ?, ?)', (username, password_hash,email,phone_number,registration_date, role,default_shipping_address))
    conn.commit()
    customer_id = cur.lastrowid
    conn.close()
    return customer_id
def update_user(users_id,username, password_hash,email,phone_number, role,default_shipping_address):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE Users SET username = ?, password_hash = ?, email = ?, phone_number = ?, registration_date = ?, role = ? , default_shipping_address = ? WHERE user_id = ?', (users_id,username, password_hash,email,phone_number, role,default_shipping_address))
    conn.commit()
    conn.close()
    return get_users(id)
def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM Users WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()


# users CRUD routes
@app.route('/Users', methods=['GET'])
def list_users():
    customers = get_all_users()
    response = jsonify(customers)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    response.headers['Content-Range'] = len(customers)
    return response

@app.route('/Users/<int:user_id>', methods=['GET'])
def get_customer_by_id(user_id):
    user = get_users(user_id)
    if user is None:
        return '', 404
    return jsonify(user), 200

@app.route('/Users', methods=['POST'])
def add_customer():
    username = request.json['username']
    password_hash = request.json['password_hash']
    email = request.json['email']
    phone_number = request.json['phone_number']
    role = request.json['role']
    default_shipping_address = request.json['default_shipping_address']
    user_id = create_user(username, password_hash,email,phone_number, role,default_shipping_address)
    return jsonify(get_users(user_id)), 201

@app.route('/Users/<int:user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    username = request.json['username']
    password_hash = request.json['password_hash']
    email = request.json['email']
    phone_number = request.json['phone_number']
    role = request.json['role']
    default_shipping_address = request.json['default_shipping_address']
    registration_date = request.json['registration_date']
    updated = update_user(user_id,username, password_hash,email,phone_number, registration_date,role,default_shipping_address)
    return jsonify(updated), 200

@app.route('/Users/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    delete_user(user_id)
    return jsonify({"user_id":user_id}), 200


#-------------------------------------------------



if __name__ == '__main__':
    app.run(debug=True)