import mysql.connector
import configparser
from mysql.connector import Error
from prettytable import PrettyTable

# Read MySQL configuration from mysql.properties
config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host')
dbname = config.get('DatabaseSection', 'db.schema')
username = config.get('DatabaseSection', 'db.username')
password = config.get('DatabaseSection', 'db.password')
port = config.get('DatabaseSection', 'db.port')

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host=dburl,
        database=dbname,
        user=username,
        password=password,
        port=port
    )

    if conn.is_connected():
        print('Connected to MySQL database')

        # Perform SQL query
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM item')

        # Fetch all rows
        rows = cursor.fetchall()

        # Create a PrettyTable instance
        table = PrettyTable()
        table.field_names = [i[0] for i in cursor.description]

        # Add rows to the table
        for row in rows:
            table.add_row(row)

        # Print the table
        print(table)

except Error as e:
    print(f'Error connecting to MySQL: {e}')

finally:
    # Close connection
    if conn.is_connected():
        cursor.close()
        conn.close()
        print('MySQL connection closed')
