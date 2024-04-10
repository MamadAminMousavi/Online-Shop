from flask import Flask, jsonify , request
import sqlite3
from flask_cors import CORS, cross_origin
import io
import psycopg2
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


#category crud function
def get_all_Categories():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Categories')
    Categories = cur.fetchall()
    final_Categories = []
    for Categorie in Categories:
        final_Categories.append({
            "category_id": Categorie[0],
            "name": Categorie[1],
            "description": Categorie[2],
            "parent_category_id": Categorie[3],
            "created_at": Categorie[4],
        })
    conn.close()
    return final_Categories
def create_Categories(name, description, parent_category_id):
    conn = get_db_connection()
    cur = conn.cursor()
    created_at = datetime.today().strftime('%Y-%m-%d')
    cur.execute('INSERT INTO Categories (name, description,parent_category_id,created_at) VALUES (?, ?, ?, ?)', (name, description, parent_category_id, created_at))
    conn.commit()
    conn.close()
    return "ok"
def get_Categories(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Categories WHERE category_id = ?',(id,))
    Categorie = cur.fetchone()
    conn.close()
    final_category = {
        "category_id": Categorie[0],
        "name": Categorie[1],
        "description": Categorie[2],
        "parent_category_id": Categorie[3],
        "created_at": Categorie[4],
    }
    return final_category
def delete_category(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM Categories WHERE category_id = ?', (id,))
    conn.commit()
    conn.close()
def update_category(name,description,parent_category_id,created_at,id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE Categories SET name = ?, description = ?, parent_category_id = ?, created_at = ? WHERE category_id = ?', (name,description,parent_category_id,created_at,id))
    conn.commit()
    conn.close()
    return get_Categories(id)


# category crud routes
@app.route('/Categories', methods=['GET'])
def list_Categories():
    Categories = get_all_Categories()
    response = jsonify(Categories)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    response.headers['Content-Range'] = len(Categories)
    return response
@app.route('/Category/<int:id>', methods=['GET'])
def Category(id):
    Category = get_Categories(id)
    if Category is None:
        return '', 404
    return jsonify(Category), 200
@app.route('/Categories', methods=['POST'])
def add_Categories():
    name = request.json['name']
    description = request.json['description']
    parent_category_id = request.json['parent_category_id']
    Categories_id = create_Categories(name, description, parent_category_id)
    return "ok", 201
@app.route('/Category/<int:id>', methods=['DELETE'])
def delete_category_by_id(id):
    delete_category(id)
    return jsonify({"id":id}), 200
@app.route('/Category/<int:id>', methods=['PUT'])
def update_category_by_id(id):
    name = request.json['name']
    description = request.json['description']
    parent_category_id = request.json['parent_category_id']
    created_at = request.json['created_at']
    updated = update_category(name, description, parent_category_id, created_at,id)
    return jsonify(updated), 200


#-------------------------------------------------


#order crud function
#order crud function
def get_all_orders():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Orders')
    orders = cur.fetchall()
    final_orders = []
    for order in orders:
        final_orders.append({
            "order_id": order[0],
            "user_id": order[1],
            "order_date": order[2].strftime('%Y-%m-%d %H:%M:%S'),
            "total_amount": order[3],
            "status": order[4],
    })
    conn.close()
    return final_orders

def create_order(user_id, order_date, total_amount, status):
    conn = get_db_connection()
    cur = conn.cursor()
    order_date_str = order_date.strftime('%Y-%m-%d %H:%M:%S')
    cur.execute('INSERT INTO Orders (customer_id, order_date, total_amount, status) VALUES (?, ?, ?, ?)', (user_id, order_date_str, total_amount, status))
    conn.commit()
    conn.close()
    return "ok"

def get_order(order_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Orders WHERE order_id = ?', (order_id,))
    order = cur.fetchone()
    conn.close()
    if order is None:
        return None
    return {
        "order_id": order[0],
        "user_id": order[1],
        "order_date": order[2].strftime('%Y-%m-%d %H:%M:%S'),
        "total_amount": order[3],
        "status": order[4],
    }

def delete_order(order_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM Orders WHERE order_id = ?', (order_id,))
    conn.commit()
    conn.close()
    return "ok"

def update_order(order_id, customer_id, order_date, total_amount, status):
    conn = get_db_connection()
    cur = conn.cursor()
    update_stmt = "UPDATE Orders SET "
    update_params = []
    if customer_id is not None:
        update_stmt += "customer_id = ?, "
        update_params.append(customer_id)
    if order_date is not None:
        order_date_str = order_date.strftime('%Y-%m-%d %H:%M:%S')
        update_stmt += "order_date = ?, "
        update_params.append(order_date_str)        

#order crud routes
@app.route('/orders', methods=['GET'])
def list_orders():
    orders = get_all_orders()
    response = jsonify(orders)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    response.headers['Content-Range'] = len(orders)
    return response

@app.route('/Order/<int:order_id>', methods=['GET'])
def order(order_id):
    order = get_order(order_id)
    if order is None:
        return '', 404
    return jsonify(order), 200

@app.route('/Orders', methods=['POST'])
def add_order():
    user_id = request.json['customer_id']
    order_date_str = request.json['order_date']
    order_date = datetime.strptime(order_date_str, '%Y-%m-%d %H:%M:%S')
    total_amount = request.json['total_amount']
    status = request.json['status']
    order_id = create_order(user_id, order_date, total_amount, status)
    return jsonify({"order_id": order_id}), 201

@app.route('/Order/<int:order_id>', methods=['DELETE'])
def delete_order_by_id(order_id):
    delete_order(order_id)
    return jsonify({"id": order_id}), 200

@app.route('/Order/<int:order_id>', methods=['PUT'])
def update_order_by_id(order_id):
    user_id = request.json['customer_id']
    order_date_str = request.json['order_date']
    order_date = datetime.strptime(order_date_str, '%Y-%m-%d %H:%M:%S')
    total_amount = request.json['total_amount']
    status = request.json['status']
    updated_order = update_order(order_id, user_id, order_date, total_amount, status)
    return jsonify(updated_order), 200



#-------------------------------------------------


#payment crud function
def get_all_Payments():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Payments')
    Payments = cur.fetchall()
    final_Payments = []
    for Payment in Payments:
        final_Payments.append({
            "payment_id": Payment[0],
            "order_id": Payment[1],
            "payment_method": Payment[2],
            "amount": Payment[3],
            "payment_date": Payment[4],
        })
    conn.close()
    return final_Payments

def get_Payment(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Payments WHERE payment_id = ?',(id,))
    Payment = cur.fetchone()
    conn.close()
    final_Payment = {
        "category_id": Payment[0],
        "name": Payment[1],
        "description": Payment[2],
        "parent_category_id": Payment[3],
        "created_at": Payment[4],
    }
    return final_Payment

def create_one_payment(order_id, payment_method, amount): 
    conn = get_db_connection() 
    cur = conn.cursor() 
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    cur.execute('INSERT INTO Payments (order_id, payment_method, amount, payment_date) VALUES (?, ?, ?, ?)', (order_id, payment_method, amount, current_datetime)) 
    conn.commit() 
    conn.close() 
    return "ok" 

def delete_payment(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM Payments WHERE payment_id = ?', (id,))
    conn.commit()
    conn.close()

def update_payment(order_id, payment_method, amount,id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE Payments SET order_id = ?, payment_method = ?, amount = ? WHERE payment_id = ?', (order_id,payment_method,amount,id))
    conn.commit()
    conn.close()
    return get_Payment(id)

# Payments routes
@app.route('/Payments', methods=['GET'])
def list_Payments():
    Payments = get_all_Payments()
    response = jsonify(Payments)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    response.headers['Content-Range'] = len(Payments)
    return response

@app.route('/Payment/<int:id>', methods=['GET'])
def Payment(id):
    Payments = get_Payment(id)
    if Payments is None:
        return '', 404
    return jsonify(Payments), 200

@app.route('/payment', methods=['POST']) 
def create_payment(): 
    data = request.get_json() 
    order_id = data['order_id'] 
    payment_method = data['payment_method'] 
    amount = data['amount'] 
    result = create_one_payment(order_id, payment_method,amount)
    return jsonify({"message": result})

@app.route('/payment/<int:id>', methods=['DELETE'])
def delete_payment_by_id(id):
    delete_payment(id)
    return jsonify({"id":id}), 200

@app.route('/payment/<int:id>', methods=['PUT'])
def update_payment_by_id(id):
    data = request.get_json() 
    order_id = data['order_id']
    payment_method = data['payment_method'] 
    amount = data['amount'] 
    updated = update_payment(order_id, payment_method, amount,id)
    return jsonify(updated), 200


#-------------------------------------------------


#order-detail crud function
def get_all_orderDetail():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM OrderDetails')
    details = cur.fetchall()
    final_details = []
    for detail in details:
        final_details.append({
            "order_detail_id": detail[0],
            "order_id": detail[1],
            "product_id": detail[2],
            "quantity": detail[3],
            "unit_price": detail[4],
        })
    conn.close()
    return final_details

def get_details(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM OrderDetails WHERE order_detail_id = ?',(id,))
    detail = cur.fetchone()
    conn.close()
    final_details = {
            "order_detail_id": detail[0],
            "order_id": detail[1],
            "product_id": detail[2],
            "quantity": detail[3],
            "unit_price": detail[4],
    }
    return final_details

def create_detail(order_id, product_id,quantity,unit_price):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO OrderDetails (order_id,product_id,quantity,unit_price) VALUES (?, ?, ?,?)', (order_id,product_id,quantity,unit_price,))
    conn.commit()
    conn.close()
    return "ok"

def delete_detail(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM OrderDetails WHERE order_detail_id = ?', (id,))
    conn.commit()
    conn.close()
    
def update_detail(order_id, product_id,quantity,unit_price,id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE OrderDetails SET order_id = ?, product_id = ?, quantity = ?, unit_price = ? WHERE order_detail_id = ?', (order_id, product_id,quantity,unit_price,id))
    conn.commit()
    conn.close()
    return get_details(id)


# order-detail routes
@app.route('/details', methods=['GET'])
def list_details():
    details = get_all_orderDetail()
    response = jsonify(details)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    response.headers['Content-Range'] = len(details)
    return response

@app.route('/detail/<int:id>', methods=['GET'])
def detail(id):
    detail = get_details(id)
    if detail is None:
        return '', 404
    return jsonify(detail), 200

@app.route('/newDetail', methods=['POST'])
def add_details():
    order_id = request.json['order_id']
    product_id = request.json['product_id']
    quantity = request.json['quantity']
    unit_price = request.json['unit_price']
    detail_id = create_detail(order_id, product_id, quantity,unit_price)
    return "ok", 201

@app.route('/delDetail/<int:id>', methods=['DELETE'])
def delete_detail_by_id(id):
    delete_detail(id)
    return jsonify({"id":id}), 200

@app.route('/upDetail/<int:id>', methods=['PUT'])
def update_detail_by_id(id):
    order_id = request.json['order_id']
    product_id = request.json['product_id']
    quantity = request.json['quantity']
    unit_price = request.json['unit_price']
    updated = update_detail(order_id, product_id, quantity,unit_price,id)
    return jsonify(updated), 200


#-------------------------------------------------

#feedback crud function
def get_all_feedbacks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Feedback')
    feedbacks = cur.fetchall()
    final_feedbacks = []
    for feedback in feedbacks:
        final_feedbacks.append({
            "feedback_id": feedback[0],
            "customer_id": feedback[1],
            "order_id": feedback[2],
            "rating": feedback[3],
            "comment": feedback[4],
            "feedback_date": feedback[5],
        })
    conn.close()
    return final_feedbacks

def get_feedback(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM feedback WHERE feedback_id = ?',(id,))
    feedback = cur.fetchone()
    conn.close()
    final_feedback = {
            "feedback_id": feedback[0],
            "customer_id": feedback[1],
            "order_id": feedback[2],
            "rating": feedback[3],
            "comment": feedback[4],
            "feedback_date": feedback[5],
    }
    return final_feedback

def create_feedback(customer_id, order_id,rating,comment):
    conn = get_db_connection()
    cur = conn.cursor()
    created_at = datetime.today().strftime('%Y-%m-%d')
    cur.execute('INSERT INTO Feedback (customer_id, order_id,rating,comment,feedback_date) VALUES (?, ?, ?, ?,?)', (customer_id, order_id,rating,comment, created_at))
    conn.commit()
    conn.close()
    return "ok"

def delete_Feedback(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM Feedback WHERE feedback_id = ?', (id,))
    conn.commit()
    conn.close()
    
def update_Feedback(customer_id, order_id,rating,comment,id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE Feedback SET customer_id = ?, order_id = ?, rating = ?, comment = ? WHERE feedback_id = ?', (customer_id, order_id,rating,comment,id))
    conn.commit()
    conn.close()
    return get_feedback(id)

# feedback routes
@app.route('/feedbacks', methods=['GET'])
def list_feedback():
    feedback_result = get_all_feedbacks()
    response = jsonify(feedback_result)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    response.headers['Content-Range'] = len(feedback_result)
    return response

@app.route('/feedback/<int:id>', methods=['GET'])
def feedback(id):
    feedback = get_feedback(id)
    if feedback is None:
        return '', 404
    return jsonify(feedback), 200

@app.route('/feedback', methods=['POST'])
def add_feedback():
    customer_id = request.json['customer_id']
    order_id = request.json['order_id']
    rating = request.json['rating']
    comment = request.json['comment']
    if rating > 5 or rating < 1:
        return  jsonify({"error":"out of range"})
    feedback_id = create_feedback(customer_id, order_id,rating,comment)
    return "ok", 201

@app.route('/feedback/<int:id>', methods=['DELETE'])
def delete_feedback_by_id(id):
    delete_Feedback(id)
    return jsonify({"id":id}), 200

@app.route('/feedback/<int:id>', methods=['PUT'])
def update_feedback_by_id(id):
    customer_id = request.json['customer_id']
    order_id = request.json['order_id']
    rating = request.json['rating']
    comment = request.json['comment']
    updated = update_Feedback(customer_id, order_id,rating,comment,id)
    return jsonify(updated), 200


#-------------------------------------------------

#ShippingAddresses crud function
def get_all_ShippingAddresses():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM ShippingAddresses')
    ShippingAddresses = cur.fetchall()
    final_ShippingAddresses = []
    for address in ShippingAddresses:
        final_ShippingAddresses.append({
            "address_id": address[0],
            "customer_id": address[1],
            "recipient_name": address[2],
            "address_line1": address[3],
            "address_line2": address[4],
            "city": address[5],
            "state": address[6],
            "postal_code": address[7],
            "country": address[8]
        })
    conn.close()
    return final_ShippingAddresses

def get_ShippingAddresses(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM ShippingAddresses WHERE address_id = ?',(id,))
    ShippingAddresses = cur.fetchone()
    conn.close()
    final_ShippingAddresses = {
            "address_id": ShippingAddresses[0],
            "customer_id": ShippingAddresses[1],
            "recipient_name": ShippingAddresses[2],
            "address_line1": ShippingAddresses[3],
            "address_line2": ShippingAddresses[4],
            "city": ShippingAddresses[5],
            "state": ShippingAddresses[6],
            "postal_code": ShippingAddresses[7],
            "country": ShippingAddresses[8]
    }
    return final_ShippingAddresses

def create_ShippingAddresses(customer_id, recipient_name, address_line1,address_line2, city, state,postal_code,country):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO ShippingAddresses (customer_id, recipient_name, address_line1,address_line2, city, state,postal_code,country) VALUES (?, ?, ?, ?,?, ?, ?, ?)', (customer_id, recipient_name, address_line1,address_line2, city, state,postal_code,country))
    conn.commit()
    conn.close()
    return "ok"

def delete_ShippingAddresses(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM ShippingAddresses WHERE address_id = ?', (id,))
    conn.commit()
    conn.close()

def update_ShippingAddresses(customer_id, recipient_name, address_line1,address_line2, city, state,postal_code,country,id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE ShippingAddresses SET customer_id = ?, recipient_name = ?, address_line1 = ?, address_line2 = ? ,city = ?, state = ?, postal_code = ?, country = ? WHERE address_id = ?', (customer_id, recipient_name, address_line1,address_line2, city, state,postal_code,country,id))
    conn.commit()
    conn.close()
    return get_ShippingAddresses(id)

# ShippingAddresses routes
@app.route('/shipAddress', methods=['GET'])
def list_ShippingAddresses():
    ShippingAddresses = get_all_ShippingAddresses()
    response = jsonify(ShippingAddresses)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    response.headers['Content-Range'] = len(ShippingAddresses)
    return response

@app.route('/shipAddress/<int:id>', methods=['GET'])
def one_ShippingAddresses(id):
    ShippingAddresses = get_ShippingAddresses(id)
    if ShippingAddresses is None:
        return '', 404
    return jsonify(ShippingAddresses), 200

@app.route('/shipAddress', methods=['POST'])
def add_ShippingAddresses():
    customer_id = request.json['customer_id']
    recipient_name = request.json['recipient_name']
    address_line1 = request.json['address_line1']
    address_line2 = request.json['address_line2']
    city = request.json['city']
    state = request.json['state']
    postal_code = request.json['postal_code']
    country = request.json['country']
    ShippingAddresses_id = create_ShippingAddresses(customer_id, recipient_name, address_line1,address_line2, city, state,postal_code,country)
    return "ok", 201

@app.route('/shipAddress/<int:id>', methods=['DELETE'])
def delete_ShippingAddresses_by_id(id):
    delete_ShippingAddresses(id)
    return jsonify({"id":id}), 200

@app.route('/shipAddress/<int:id>', methods=['PUT'])
def update_ShippingAddresses_by_id(id):
    customer_id = request.json['customer_id']
    recipient_name = request.json['recipient_name']
    address_line1 = request.json['address_line1']
    address_line2 = request.json['address_line2']
    city = request.json['city']
    state = request.json['state']
    postal_code = request.json['postal_code']
    country = request.json['country']
    updated = update_ShippingAddresses(customer_id, recipient_name, address_line1,address_line2, city, state,postal_code,country,id)
    return jsonify(updated), 200


#-------------------------------------------------






if __name__ == '__main__':
    app.run(debug=True)