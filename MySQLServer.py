import mysql.connector

def create_database():
    connection = None
    try:
        # Establishing the connection to the MySQL server
        # Please update 'user' and 'password' with your local MySQL credentials
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )

        cursor = connection.cursor()

        # Using CREATE DATABASE IF NOT EXISTS to prevent failure if it already exists
        # SQL keywords are in UPPERCASE as per best practices
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Handling connection and execution errors
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Closing the cursor and connection to free up resources
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()