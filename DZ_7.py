import sqlite3

hw_db = '''hw.db'''
# def create_connection(db_file):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_file)
#     except sqlite3.Error as error:
#         print(error)
#     return connection
#
# def create_table(connection, sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql)
#     except sqlite3.Error as error:
#         print(error)

def create_table(sql):
    try:
        with sqlite3.connect(hw_db) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)


def insert_employees(employees):
    sql = '''INSERT INTO employees(product_title,price,quantitu) 
    VALUES(?,?,?)'''
    try:
        with sqlite3.connect(hw_db) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, employees)
    except sqlite3.Error as error:
        print(error)


def update_employees(employees):
    sql = '''UPDATE employees SET price = ?,quantitu = ? WHERE id = ?'''
    try:
        with sqlite3.connect(hw_db) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, employees)
    except sqlite3.Error as error:
        print(error)


def delete_employees(id):
    sql = '''DELETE FROM employees WHERE id = ?'''
    try:
        with sqlite3.connect(hw_db) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as error:
        print(error)


def select_all_employees():
    sql = '''SELECT product_title FROM employees'''
    try:
        with sqlite3.connect(hw_db) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as error:
        print(error)


def select_employees_price(price_limit):
    sql = '''SELECT price FROM employees WHERE price >= ?'''
    try:
        with sqlite3.connect(hw_db) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (price_limit,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as error:
        print(error)

products_table = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0,
    quantitu FLOAT NOT NULL DEFAULT 0
)
'''


# create_table(products_table)
# insert_employees(('Banana', 159.0,1))
# insert_employees(('Apple', 130.0,1))
# insert_employees(('Qear', 145.0,1))
# insert_employees(('Raspberry', 240.0,1))
# insert_employees(('Strawberry', 255.0,1))
# insert_employees(('Cherry', 305.0,1))
# insert_employees(('Mandarin', 270.0,1))
# insert_employees(('Pineapple', 270.0,1))
# insert_employees(('Lemon ', 140.99,1))
# insert_employees(('Kiwi', 310.0,1))
# insert_employees(('Pomegranate', 263.0,1))
# insert_employees(('Persimmon', 320.0,1))
# insert_employees(('Coconut', 345.0,1))
# insert_employees(('Papaya', 333.33,1))
# insert_employees(('Avocado', 300.0,1))
# insert_employees(('Apricot', 276.0,1))
# insert_employees(('Lime', 290.0,1))
# insert_employees(('Peach', 269.0,1))
# insert_employees(('Mango', 320.0,1))

#Добавить изменения функции
# update_employees((320,10,10))
# update_employees((20,1))
# update_employees((34,2))
# update_employees((53,3))
# update_employees((34,4))
# update_employees((23,5))
# update_employees((25,6))
# update_employees((34,7))
# update_employees((24,8))
# update_employees((20,9))
# update_employees((50,11))
# update_employees((30,12))
# update_employees((20,13))
# update_employees((30,14))
# update_employees((10,15))
# update_employees((10,16))
# update_employees((10,17))
# update_employees((10,18))
# update_employees((10,19))
#Удалить обьект по id
# delete_employees(3)

#распечатать в командном строке
# select_all_employees()


# select_employees_price(300)

# my_connection = create_connection(hw_db)
# if my_connection is not None:
#     print('Connection to database')
#     create_table(my_connection, products_table)
#     my_connection.close()

