import mysql.connector
import random

# MySQL database connection settings
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "ADMIN",
    "database": "tm"
}

# Initialize a MySQL connection
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Set the initial ID number
current_id = 0

# Keep track of generated IDs to avoid duplicates
generated_ids = set()

def generate_unique_id():
    global current_id
    
    while True:
        # Increment the ID number
        current_id += 1

        # Generate the full ID by adding "TTM" as a prefix
        new_id = f"TTM183W{random.randint(100,999)}"

        # Check if the generated ID is unique
        if new_id not in generated_ids:
            generated_ids.add(new_id)
            return new_id

try:
    # Create a table to store the IDs if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_ids (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ttm_id VARCHAR(10) NOT NULL
    )
    """
    cursor.execute(create_table_query)
    connection.commit()

    # Generate and store 10 unique IDs in the database
    for _ in range(1):
        unique_id = generate_unique_id()
        # Check if the ID is unique in the database
        check_query = "SELECT * FROM user_ids WHERE ttm_id = %s"
        cursor.execute(check_query, (unique_id,))
        existing_id = cursor.fetchone()

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    # Close the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
