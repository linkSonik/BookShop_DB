import mysql.connector

# ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ К БД

def search_book_janr(conn, janr):
    sql = """
    SELECT Название, Автор, Жанр, Год_издания, Стоимость FROM book WHERE Жанр = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (janr,))
    results = cur.fetchmany(10)
    print('Вот несколько книг с данным жанром')
    for row in results:
        print(row,'\n')

def search_book_avtor(conn, avtor):
    sql = """
    SELECT Название, Автор, Жанр, Год_издания, Стоимость FROM book WHERE Автор = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (avtor,))
    results = cur.fetchmany(10)
    print('Вот несколько книг написанных данным автором')
    for row in results:
        print(row,'\n')

def search_book_year(conn, year):
    sql = """
    SELECT Название, Автор, Жанр, Год_издания, Стоимость FROM book WHERE Год_издания = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (year,))
    results = cur.fetchmany(10)
    print('Вот несколько книг изданных в данном году')
    for row in results:
        print(row,'\n')

def search_book_cost(conn, cost1, cost2):
    sql = """
    SELECT Название, Автор, Жанр, Год_издания, Стоимость FROM book WHERE Стоимость BETWEEN %s and %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (cost1, cost2,))
    results = cur.fetchmany(10)
    print('Вот несколько книг в таком ценовом диапазоне')
    for row in results:
        print(row,'\n')

# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ book
def create_book(conn, book):
    sql = """
    # INSERT INTO book(Название, Автор, Жанр, Год_издания, Стоимость, order_order_id, specifications_specifications_id, werehouse_werehouse_id, supplier_supplier_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()

def get_book(conn, book_id):
    sql = """
    SELECT *
    FROM book
    WHERE book_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (book_id,))
    return cur.fetchone()

def update_book(conn, book):
    sql = """
    UPDATE book
    SET Название = %s, Автор = %s, Жанр = %s, Год_издания = %s, Стоимость = %s, order_order_id = %s, specifications_specifications_id = %s, werehouse_werehouse_id = %s, supplier_supplier_id = %s
    WHERE book_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()

def delete_book(conn, book_id):
    sql1 = "UPDATE difect set book_book_id = NULL WHERE book_book_id = %s"
    sql2 = "DELETE FROM book WHERE book_id = %s"
    cur = conn.cursor()
    cur.execute(sql1, (book_id,))
    cur.execute(sql2, (book_id,))
    conn.commit()

# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ client
def create_client(conn, client):
    sql = """
    INSERT INTO client(ФИО, Номер_телефона, Email, Датв_продажи)
    VALUES (%s, %s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()

def get_client(conn, client_id):
    sql = """
    SELECT * 
    FROM client
    WHERE client_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (client_id,))
    return cur.fetchone()

def update_client(conn, client):
    sql = """
    UPDATE client
    SET ФИО = %s, Номер_телефона = %s, Email = %s, Датв_продажи = %s
    WHERE client_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()

def delete_client(conn, client_id):
    sql1 = "DELETE FROM bookshop.order WHERE bookshop.order.client_client_id = %s"
    sql2 = "DELETE FROM client WHERE client_id = %s"
    cur = conn.cursor()
    cur.execute(sql1, (client_id,))
    cur.execute(sql2, (client_id,))
    conn.commit()

# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ order
def create_order(conn, order):
    sql = """
    INSERT INTO bookshop.order(Дата_оформления, Дата_выдачи, worker_worker_id, client_client_id)
    VALUES (%s, %s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, order)
    conn.commit()

def get_order(conn, order):
    sql = """
    SELECT order_id, Дата_оформления, Дата_выдачи, client_client_id as client_id, client.ФИО as Заказчик
    FROM bookshop.order
    JOIN client ON bookshop.order.client_client_id = client.client_id
    WHERE order_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (order,))
    return cur.fetchone()

def update_order(conn, order):
    sql = """
    UPDATE bookshop.order
    SET Дата_оформления = %s, Дата_выдачи = %s, worker_worker_id = %s, client_client_id = %s
    WHERE order_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, order)
    conn.commit()


def delete_order(conn, order):
    sql1 = "UPDATE book SET order_order_id = NULL WHERE order_order_id = %s"
    sql2 = "UPDATE officesupplies SET order_order_id = NULL WHERE order_order_id = %s"
    sql3 = "DELETE FROM bookshop.order WHERE order_id = %s"
    cur = conn.cursor()
    cur.execute(sql1, (order,))
    cur.execute(sql2, (order,))
    cur.execute(sql3, (order,))
    conn.commit()


# ФУНКЦИИ ДЛЯ ПОДКЛЮЧЕНИЯ И ОТКЛЮЧЕНИЯ ОТ БД
def connect_to_db(host, user, password, database):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(f"Успешное подключение к {database} с помощью MySQL Connector/Python\n")
    except Exception as e:
        print(f"Произошла ошибка при подключении к базе данных: {e}")
    return conn

def close_connection(conn):
    if conn:
        conn.close()
        print("\nСоединение с базой данных закрыто")


# ОСНОВНАЯ ФУНКЦИЯ РАБОТЫ С ПОЛЬЗОВАТЕЛЕМ ПРОГРАММЫ
def main():
    host = "localhost"
    user = "root"
    password = "вкуфьифы0943"
    database = "BookShop"
    conn = connect_to_db(host, user, password, database)

    while True:
        print("\nВыберите таблицу с которой хотите взаимодействовать \n или одно из функциональных требований:")
        print("1) order")
        print("2) client")
        print("3) book")
        print(" ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ")
        print("4) Поиск книги по жанру")
        print("5) Поиск книги по автору")
        print("6) Поиск книги по году издания")
        print("7) Поиск книги по ценовому диаапазону")
        print("8) Выход")
        table_choice = input("Введите номер пункта: ")

        if table_choice == '8':
            break
        if(table_choice == '1' or table_choice == '2' or table_choice == '3' ):
            print("\nВыберите действие:")
            print("1) Добавить запись")
            print("2) Просмотреть запись")
            print("3) Обновить запись")
            print("4) Удалить запись")
            print("5) Назад")
            action_choice = input("Введите номер пункта: ")
            if action_choice == '5':
                continue


        if table_choice == '1':  # order
            
            if action_choice == '1':
                new_order = tuple(input("Введите данные заказа через запятую(Дата_оформления, Дата_выдачи, worker_worker_id, client_client_id): ").split(','))
                create_order(conn, new_order)
            
            elif action_choice == '2':
                ID_order = input("Введите ID заказа: ")
                order = get_order(conn, ID_order)
                print(order)
            
            elif action_choice == '3':
                updated_order_id = input("Введите ID заказа для обновления: ")
                updated_order = list(input("Введите обновленные данные заказа через запятую(Дата_оформления, Дата_выдачи, worker_worker_id, client_client_id): ").split(','))
                updated_order.append(updated_order_id)
                updated_order_tuple = tuple(updated_order)
                update_order(conn, updated_order_tuple)
            
            elif action_choice == '4':
                ID_order_del = input("Введите ID заказа для удаления: ")
                delete_order(conn, ID_order_del)
        
        
        elif table_choice == '2':  # client
            
            if action_choice == '1':
                new_client = tuple(input("Введите данные клиента через запятую(ФИО, Номер_телефона, Email, Датв_продажи): ").split(','))
                create_client(conn, new_client)
            
            elif action_choice == '2':
                ID_client = input("Введите ID клиента: ")
                client = get_client(conn, ID_client)
                print(client)
            
            elif action_choice == '3':
                updated_client_id = input("Введите ID клиента для обновления: ")
                updated_client = list(input("Введите обновленные данные клиента через запятую(ФИО, Номер_телефона, Email, Датв_продажи): ").split(','))
                updated_client.append(updated_client_id)
                updated_client_tuple = tuple(updated_client)
                update_client(conn, updated_client_tuple)
            
            elif action_choice == '4':
                ID_client_del = input("Введите ID клиента для удаления: ")
                delete_client(conn, ID_client_del)
        
        
        elif table_choice == '3':  # book
            
            if action_choice == '1':
                new_book = tuple(input("Введите информацию о книге через запятую\n(Название, Автор, Жанр, Год_издания, Стоимость, order_order_id, specifications_specifications_id, werehouse_werehouse_id, supplier_supplier_id): ").split(','))
                create_book(conn, new_book)
            
            elif action_choice == '2':
                ID_book = input("Введите ID книги: ")
                book = get_book(conn, ID_book)
                print(book)
            
            elif action_choice == '3':
                updated_book_id = input("Введите ID книги для обновления: ")
                updated_book = list(input("Введите обновленную информацию о книге через запятую\n(Название, Автор, Жанр, Год_издания, Стоимость, order_order_id, specifications_specifications_id, werehouse_werehouse_id, supplier_supplier_id): ").split(','))
                updated_book.append(updated_book_id)
                updated_book_tuple = tuple(updated_book)
                update_book(conn, updated_book_tuple)
            
            elif action_choice == '4':
                ID_book_del = input("Введите ID книги: ")
                delete_book(conn, ID_book_del)

        elif table_choice == '4':
            janr = input("Введите жанр книги: ")
            search_book_janr(conn, janr)
            continue

        elif table_choice == '5':
            avtor = input("Введите автора книги: ")
            search_book_avtor(conn, avtor)
            continue

        elif table_choice == '6':
            year = input("Введите год издания книги: ")
            search_book_year(conn, year)
            continue

        elif table_choice == '7':
            cost1 = input("Введите начало ценового диапазона: ")
            cost2 = input("Введите конец ценового диапазона: ")
            search_book_cost(conn, cost1, cost2)
            continue
        else:
            print("Неверный пункт. Пожалуйста, попробуйте еще раз.")

    close_connection(conn)

if __name__ == "__main__":
    main()