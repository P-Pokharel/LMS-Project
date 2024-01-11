import mysql.connector

query_status = False
db_cursor = None

def database_cursor(query):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lms_db"
    )
    db_cursor = connection.cursor()
    db_cursor.execute(query)
    # connection.commit()
    # connection.close()
    query_status = True

    return query_status

def fetch_info(book_table):
    rows = db_cursor.fetchall()
    for record in rows:
        book_table.insert(record)


def connection_terminator():
    connection.commit()
    connection.close()
