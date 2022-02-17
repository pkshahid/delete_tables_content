import psycopg2
import copy

#establishing the connection
conn = psycopg2.connect(
   database="data_base_name", user='postgres', password='password', host='127.0.0.1', port= '5432'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving contents of the table
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
# print(cursor.fetchall())
tables = copy.deepcopy(cursor.fetchall())
#Commit your changes in the database
conn.commit()
for table in tables:
    cursor.execute(f"TRUNCATE TABLE {table[0]} CASCADE;")
    print(f"Deleted {table[0]} contents")
    conn.commit()

#Closing the connection
conn.close()