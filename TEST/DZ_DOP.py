import sqlite3


conn = sqlite3.connect('DZ.db')
cursor = conn.cursor()



def show_stores():
    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()
    print("Список магазинов:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")



def show_products_in_store(store_id):
    query = """
    SELECT products.title, categories.title, products.unit_price, products.stock_quantity
    FROM products
    JOIN categories ON products.category_code = categories.code
    WHERE products.store_id = ?
    """
    cursor.execute(query, (store_id,))
    products = cursor.fetchall()

    if products:
        for product in products:
            print(f"\nНазвание продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")
    else:
        print("Продукты в этом магазине не найдены.")



def main():
    while True:
        print(
            "\nВы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0.")
        show_stores()

        try:
            store_id = int(input("\nВведите id магазина: "))
            if store_id == 0:
                print("Выход из программы.")
                break
            show_products_in_store(store_id)
        except ValueError:
            print("Пожалуйста, введите корректный id магазина.")



# if __name__ == "__main__":
#     main()


conn.close()