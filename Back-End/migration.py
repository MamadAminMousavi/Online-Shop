import os
import sqlite3

# Specify the path where the SQLite database file will be created
database_path = 'Online-Shop/Back-End/Online-shop.db'

# Check if the path to the database file exists, if not create the directories
os.makedirs(os.path.dirname(database_path), exist_ok=True)

# Check if the database file already exists
if not os.path.exists(database_path):
    # Connect to the database and create it if it doesn't exist
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    # Create tables
    cur.execute('''
        CREATE TABLE Users (
            user_id INTEGER PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password_hash VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            phone_number VARCHAR(15) NOT NULL,
            registration_date DATE NOT NULL,
            role VARCHAR(20) NOT NULL,
            default_shipping_address INTEGER,
            FOREIGN KEY (default_shipping_address) REFERENCES ShippingAddresses(address_id)
        )
    ''')

    cur.execute('''
        CREATE TABLE Products (
            product_id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES Categories(category_id)
        )
    ''')

    cur.execute('''
        CREATE TABLE Orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            order_date DATETIME NOT NULL,
            total_amount DECIMAL(10, 2) NOT NULL,
            status VARCHAR(20) NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
        )
    ''')

    cur.execute('''
        CREATE TABLE OrderDetails (
            order_detail_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INT NOT NULL,
            unit_price DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES Orders(order_id),
            FOREIGN KEY (product_id) REFERENCES Products(product_id)
        )
    ''')

    cur.execute('''
        CREATE TABLE Categories (
            category_id INTEGER PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            description TEXT,
            parent_category_id INTEGER,
            created_at DATETIME NOT NULL,
            FOREIGN KEY (parent_category_id) REFERENCES Categories(category_id)
        )
    ''')

    cur.execute('''
        CREATE TABLE Payments (
            payment_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            payment_method VARCHAR(50) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            payment_date DATETIME NOT NULL,
            FOREIGN KEY (order_id) REFERENCES Orders(order_id)
        )
    ''')

    cur.execute('''
        CREATE TABLE ShippingAddresses (
            address_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            recipient_name VARCHAR(100) NOT NULL,
            address_line1 VARCHAR(255) NOT NULL,
            address_line2 VARCHAR(255),
            city VARCHAR(100) NOT NULL,
            state VARCHAR(100) NOT NULL,
            postal_code VARCHAR(20) NOT NULL,
            country VARCHAR(100) NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
        )
    ''')

    cur.execute('''
        CREATE TABLE Feedback (
            feedback_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            order_id INTEGER NOT NULL,
            rating INT NOT NULL,
            comment TEXT,
            feedback_date DATETIME NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
            FOREIGN KEY (order_id) REFERENCES Orders(order_id)
        )
    ''')

    cur.execute('''
        CREATE TABLE AdminLogs (
            log_id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            action VARCHAR(100) NOT NULL,
            action_date DATETIME NOT NULL,
            ip_address VARCHAR(50) NOT NULL,
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database and tables created successfully.")
else:
    print("Database file already exists.")