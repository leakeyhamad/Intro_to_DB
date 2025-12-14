import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Establishing the connection to the MySQL server
        # Replace 'your_username' and 'your_password' with your actual credentials
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username', 
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Executing the creation command
            # IF NOT EXISTS prevents the script from failing if it already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Printing error message if connection or execution fails
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure the connection is closed properly
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()