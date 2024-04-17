import sqlite3
import random
import string

class ProductManager:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                price REAL NOT NULL
                                )''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cursor.execute('''INSERT INTO products (name, price) VALUES (?, ?)''', (name, price))
        self.conn.commit()

    def update_product(self, product_id, name, price):
        self.cursor.execute('''UPDATE products SET name = ?, price = ? WHERE id = ?''', (name, price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cursor.execute('''SELECT * FROM products WHERE id = ?''', (product_id,))
        return self.cursor.fetchone()

    def generate_sample_data(self, num_samples=100):
        for _ in range(num_samples):
            name = ''.join(random.choices(string.ascii_letters, k=8))
            price = round(random.uniform(10.0, 1000.0), 2)
            self.insert_product(name, price)

# 테스트
if __name__ == "__main__":
    manager = ProductManager()

    # 샘플 데이터 생성
    manager.generate_sample_data()

    # 특정 제품 조회
    product_id = 1
    print("Product with ID {}: {}".format(product_id, manager.select_product(product_id)))

    # 제품 업데이트
    new_name = "New Product Name"
    new_price = 999.99
    manager.update_product(product_id, new_name, new_price)
    print("Product after update: {}".format(manager.select_product(product_id)))

    # 제품 삭제
    manager.delete_product(product_id)
    print("Product deleted. Remaining products:")
    for product in manager.cursor.execute('''SELECT * FROM products'''):
        print(product)
