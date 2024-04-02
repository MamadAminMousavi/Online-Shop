from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



# Connect to the database
def get_db_connection():
    conn = sqlite3.connect('customers.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get a customer by ID
def get_customer(customer_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
    customer = cur.fetchone()
    final_customer = {
            "id": customer[0],
            "name": customer[1],
            "email": customer[2],
            "phone": customer[3],
        }
    conn.close()
    return final_customer

# Create a new customer
def create_customer(name, email, phone):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
    conn.commit()
    customer_id = cur.lastrowid
    conn.close()
    return customer_id

# Create 10 customers
# for i in range(1, 11):
#     name = f'Customer {i}'
#     email = f'customer{i}@example.com'
#     phone = f'555-123-456{i}'
#     create_customer(name, email, phone)

# Update a customer
def update_customer(customer_id, name, email, phone):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE customers SET name = ?, email = ?, phone = ? WHERE id = ?', (name, email, phone, customer_id))
    conn.commit()
    conn.close()
    return get_customer(customer_id)

# Delete a customer
def delete_customer(customer_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
    conn.commit()
    conn.close()

# Get all customers
def get_all_customers(limit):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM customers LIMIT '+str(limit))
    customers = cur.fetchall()
    final_customers = []
    for customer in customers:
        final_customers.append({
            "id": customer[0],
            "name": customer[1],
            "email": customer[2],
            "phone": customer[3],
        })
    conn.close()
    return final_customers

#test backend
@app.route('/', methods=['GET'])
def test():
    return "ok"

# CRUD routes
@app.route('/customer', methods=['GET'])
def list_customer():
    range = request.args.get('range')
    customers = get_all_customers(int(range[3])+ 1)
    response = jsonify(customers)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    response.headers['Content-Range'] = len(customers)
    return response

@app.route('/customer', methods=['POST'])
def add_customer():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']
    customer_id = create_customer(name, email, phone)
    return jsonify(get_customer(customer_id)), 201

@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    customer = get_customer(customer_id)
    if customer is None:
        return '', 404
    return jsonify(customer), 200

@app.route('/customer/<int:customer_id>', methods=['PUT'])
def update_customer_by_id(customer_id):
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']
    updated = update_customer(customer_id, name, email, phone)
    return jsonify(updated), 200

@app.route('/customer/<int:customer_id>', methods=['DELETE'])
def delete_customer_by_id(customer_id):
    delete_customer(customer_id)
    return jsonify({"id":customer_id}), 200

if __name__ == '__main__':
    app.run(debug=True)