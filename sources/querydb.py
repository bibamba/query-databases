import mysql.connector
from mysql.connector import Error
import typer 
import os 

app = typer.Typer()

# Create a connection to mysql db
def create_db_connection(dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv('HOSTNAME'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASS'),
            database=dbname
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Function to create a database
@app.command()
def create_database(dbname: str, query: str):
    connection = create_db_connection(dbname)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

# Create a query execution function
@app.command()
def execute_query(dbname: str, query: str):
    connection = create_db_connection(dbname)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

# Read data from Database
@app.command()
def read_data(dbname: str, query: str):
    connection = create_db_connection(dbname)
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
    except Error as err:
        print(f"Error: '{err}'")

    

if __name__ == "__main__":
    app()