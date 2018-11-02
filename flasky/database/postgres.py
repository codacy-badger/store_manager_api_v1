import psycopg2
import psycopg2.extras


class DataBase:
    """
    A class that cretaes a connection to a postgres database.
    connect() method creates a connection to the database.
    create_db_tables() loads database tables.
    drop_db_tables() drops/destroys database tables.
    insert() adds object data into a database table.
    check() searches for availability of a specific object and if found, returns that object.
    update() updates object values for a particular table.
    fetchone() returns a single row table objects.
    fetchmany() returns a list of row table objects.
    fetchall() returns a list of all table objects.
    delete() deletes a particular row data from the table.
    close() terminates a running database connection
    """

    def __init__(self):
        pass

    @classmethod
    def connect(cls, *args):
        try:
            cls.connection = psycopg2.connect(
                host=args[0], dbname=args[1], user=args[2], password=args[3])

            cls.cursor = cls.connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)
            print("...connected....")

        except (Exception) as error:
            cls.connection.rollback()
            cls.connection.commit()
            print('Failed to connect to the database {}'.format(error))

    @classmethod
    def create_db_tables(cls):
        token_file = "flasky/database/invalid_token_table.sql"
        users_file = "flasky/database/users_table.sql"
        product_file = "flasky/database/products_table.sql"
        cart_file = "flasky/database/cart_table.sql"
        sale_file = "flasky/database/sales_table.sql"

        token_sql = open(token_file, mode='r', encoding='utf-8').read()
        users_sql = open(users_file, mode='r', encoding='utf-8').read()
        product_sql = open(product_file, mode='r', encoding='utf-8').read()
        cart_sql = open(cart_file, mode='r', encoding='utf-8').read()
        sales_sql = open(sale_file, mode='r', encoding='utf-8').read()

        cls.cursor.execute(users_sql)
        cls.cursor.execute(product_sql)
        cls.cursor.execute(token_sql)
        cls.cursor.execute(cart_sql)
        cls.cursor.execute(sales_sql)

        cls.connection.commit()

    @classmethod
    def drop_tables(cls):
        users = "DROP TABLE IF EXISTS users CASCADE"
        products = "DROP TABLE IF EXISTS products CASCADE"
        invalidtokens = "DROP TABLE IF EXISTS invalidtokens CASCADE"
        cart = "DROP TABLE IF EXISTS cart_table CASCADE"
        sales = "DROP TABLE IF EXISTS sales CASCADE"

        cls.cursor.execute(users)
        cls.cursor.execute(products)
        cls.cursor.execute(invalidtokens)
        cls.cursor.execute(cart)
        cls.cursor.execute(sales)

        cls.connection.commit()
        print('...dropped...')

    @classmethod
    def insert(cls, insert_query, values):
        try:
            cls.cursor.execute(insert_query, values)
            cls.connection.commit()
        except (Exception) as error:
            cls.connection.rollback()
            print('Failed to insert data into table {}'.format(error))

    @classmethod
    def check(cls, select_query):
        try:
            cls.cursor.execute(select_query)
            return cls.cursor.fetchone()
        except (Exception) as error:
            if cls.connection:
                cls.connection.rollback()
            print('Failed to select table data {}'.format(error))

    @classmethod
    def update(cls, update_query):
        try:
            cls.cursor.execute(update_query)
            cls.connection.commit()
            return cls.cursor.rowcount
        except (Exception) as error:
            if cls.connection:
                cls.connection.rollback()
            print('Failed to update table data {}'.format(error))

    @classmethod
    def fetch_one(cls, fetch_one_query):
        try:
            cls.cursor.execute(fetch_one_query)
            return cls.cursor.fetchone()
        except (Exception) as error:
            if cls.connection:
                cls.connection.rollback()
            print('Failed to fetch table row data {}'.format(error))

    @classmethod
    def fetch_all(cls, fetch_all_query):
        try:
            cls.cursor.execute(fetch_all_query)
            return cls.cursor.fetchall()
        except (Exception) as error:
            if cls.connection:
                cls.connection.rollback()
            print('Failed to fetch table row data {}'.format(error))

    @classmethod
    def delete(cls, delete_query):
        try:
            cls.cursor.execute(delete_query)
            cls.connection.commit()
            return cls.cursor.rowcount
        except (Exception) as error:
            if cls.connection:
                cls.connection.rollback()
        print('Failed to delete table row data {}'.format(error))

    @classmethod
    def close(cls):
        if cls.connection:
            cls.cursor.close()
            cls.connection.close()

# create an instance of the database
db = DataBase()
