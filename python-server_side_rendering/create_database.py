import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        );
    ''')
    # Clear existing data to prevent duplicate entries
    cursor.execute('DELETE FROM Products')
    # Insert data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Headphones', 'Electronics', 199.99),
        (4, 'Notebook', 'Stationery', 5.49),
        (5, 'Smartphone', 'Electronics', 999.99),
        (6, 'Jarvis', 'AI Assistant', 2999.99)
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()