import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# connection = pymysql.connect(host='localhost',user='root',password='password',database='miniproject2',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

# Establish a database connection
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Execute SQL query
cursor.execute('SELECT * FROM product')

# Gets all rows from the result
rows = cursor.fetchall()
for row in rows:
    print(f'Product ID: {str(row[0])}, Product Name: {row[1]}, Price: {row[2]}')

# Closes the cursor so will be unusable from this point 
cursor.close()

# Closes the connection to the DB, make sure you ALWAYS do this
connection.close()