from flask import Flask, render_template
import mysql.connector
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ADMIN',
    'database': 'tm',
}

# Function to execute the SQL query and retrieve data
def execute_query():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT * FROM bus_record_2 WHERE id = 'TTM183W712';"
        cursor.execute(query)

        result = cursor.fetchone()  # Retrieve the first row of the result
        age = result[1] if result else None  # Extract the 'age' from the result
        date=result[5]
        print(date)
        print(age)
        print(result)
        cursor.close()
        connection.close()
        # Return the 'age' as a variable
    except Exception as e:
        print(e)
        return None

execute_query()