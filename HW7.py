import sqlite3
conn = sqlite3.connect('hw.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL CHECK(LENGTH(product_title) <= 200),
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
''')
conn.commit()
def add_sample_products():
    sample_products = [
        ("Мыло детское", 45.5, 10),
        ("Шампунь для волос", 120.0, 8),
        ("Гель для душа", 85.99, 15),
        ("Зубная паста", 65.0, 20),
        ("Жидкое мыло", 55.75, 5),
        ("Мыло хозяйственное", 25.0, 50),
        ("Порошок стиральный", 199.99, 7),
        ("Освежитель воздуха", 90.0, 4),
        ("Крем для рук", 70.0, 9),
        ("Туалетная бумага", 30.0, 25),
        ("Полотенца бумажные", 40.0, 12),
        ("Салфетки влажные", 35.0, 30),
        ("Дезодорант", 110.0, 6),
        ("Бальзам для губ", 60.0, 14),
        ("Крем для лица", 150.0, 3)
    ]
    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)
    ''', sample_products)
    conn.commit()
def update_quantity(product_id, new_quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()
def update_price(product_id, new_price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()
def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
def list_all_products():
    cursor.execute('SELECT * FROM products')
    for row in cursor.fetchall():
        print(row)
def find_products_by_price_and_quantity(price_limit, quantity_limit):
    cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (price_limit, quantity_limit))
    for row in cursor.fetchall():
        print(row)
def search_products_by_title(keyword):
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", (f"%{keyword}%",))
    for row in cursor.fetchall():
        print(row)
print("Добавление товаров:")
add_sample_products()
list_all_products()
print("Изменение количества товара (id = 1):")
update_quantity(1, 50)
list_all_products()
print("Изменение цены товара (id = 2):")
update_price(2, 199.99)
list_all_products()
print("Удаление товара (id = 3):")
delete_product(3)
list_all_products()
print("Товары дешевле 100 сом и количество > 5:")
find_products_by_price_and_quantity(100, 5)
print("Поиск по ключевому слову 'мыло':")
search_products_by_title("мыло")
conn.close()
