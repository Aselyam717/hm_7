import sqlite3

#1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3

#2. В БД создать таблицу products

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

bd_products = 'hw.db'


#3. В таблицу добавить поле id - первичный ключ тип данных числовой и поддерживающий авто-инкрементацию.
#4. Добавить поле product_title текстового типа данных максимальной длиной 200 символов, поле не должно быть пустым (NOT NULL)
# 5. Добавить поле price не целочисленного типа данных размером 10 цифр из которых 2 цифры после плавающей точки, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0.0
#6 Добавить поле quantity целочисленного типа данных, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0

sql_to_create_product_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL, 
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
    )
'''


#7. Добавить функцию, которая бы добавляла в БД 15 различных товаров
def insert_products(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''INSERT INTO products (product_title, price, quantity) 
                        VALUES (?, ?, ?)
            '''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)


#8. Добавить функцию, которая меняет количество товара по id
def update_quantity_by_id(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)

#9. Добавить функцию, которая меняет цену товара по id

def update_price_by_id(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''UPDATE products SET price = ? WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)

#10. Добавить функцию, которая удаляет товар по id

def delete_product(db_file, id):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''DELETE FROM products WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
        except sqlite3.Error as error:
            print(error)

#11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли

def select_all_products(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)

#12. Добавить функцию, которая бы выбирала из БД товары, которые дешевле лимита по цене (100 сом) сомов и количество которых больше чем лимит остатка на складе (5 шт) и распечатывала бы их в консоли

def select_products_byprice_byquantity(db_file, limit):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products WHERE price <= ? AND quantity >= ? '''
            cursor = connection.cursor()
            cursor.execute(sql, limit)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)

##14. Протестировать каждую написанную функцию


my_connection = create_connection(bd_products)
if my_connection:
    print('Successfully connected to database')

    create_table(my_connection, sql_to_create_product_table)


    create_table(my_connection, sql_to_create_product_table)

    # insert_products(bd_products, ('Жидкое мыло Ю', 150.0, 6))
    # insert_products(bd_products, ('Жидкое мыло A', 55.0, 25))
    # insert_products(bd_products, ('Жидкое мыло B', 350.0, 30))
    # insert_products(bd_products, ('Жидкое мыло C', 250.0, 2))
    # insert_products(bd_products, ('Жидкое мыло D', 190.0, 17))
    # insert_products(bd_products, ('Жидкое мыло E', 170.0, 666))
    # insert_products(bd_products, ('Жидкое мыло AA', 153.0, 36))
    # insert_products(bd_products, ('Жидкое мыло ЮЮ', 157.0, 46))
    # insert_products(bd_products, ('Жидкое мыло ЮЮЮ', 111.0, 56))
    # insert_products(bd_products, ('Жидкое мыло ИИИ', 170.0, 688))
    # insert_products(bd_products, ('Жидкое мыло АААА', 160.0, 776))
    # insert_products(bd_products, ('Жидкое мыло КККК', 157.0, 65))
    # insert_products(bd_products, ('Жидкое мыло Н', 55.0, 600))
    # insert_products(bd_products, ('Жидкое мыло ГГ', 550.0, 6))
    # insert_products(bd_products, ('Жидкое мыло ЗЗ', 1150.0, 6))


    # update_price_by_id(bd_products, (200, 15))
    # update_quantity_by_id(bd_products, (10, 10))
    # delete_product(bd_products, 2)

    # select_all_products(bd_products)
    select_products_byprice_byquantity(bd_products, (100, 5))

    my_connection.close()