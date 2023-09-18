import mysql.connector
from mysql.connector import Error
from secrets import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, SSL_CA

connection = None
cursor = None

try:
    connection = mysql.connector.connect(
        user=MYSQL_USER, 
        password=MYSQL_PASSWORD, 
        host=MYSQL_HOST, 
        port=MYSQL_PORT, 
        database="wsbstonk",  # Connecting to the wsbstonk schema
        ssl_disabled=False
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reddit_data LIMIT 5;")  # Querying the reddit_data table
        records = cursor.fetchall()
        if records:
            for record in records:
                print(record)
        else:
            print("No records found in the reddit_data table.")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (connection is not None and connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
