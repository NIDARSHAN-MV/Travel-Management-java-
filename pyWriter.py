from flask import Flask, render_template, request , render_template_string
import mysql.connector
import random
import idGenerator


app = Flask(__name__)

# Define your database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ADMIN',
    'database': 'tm'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Get data from the HTML form
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        mode = request.form['mode']

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        try:
            # Create a SQL query to insert data
            insert_query = "INSERT INTO user (name, email, date, mode,id) VALUES (%s, %s, %s, %s, %s)"
            data = (name, email, date, mode,idGenerator.unique_id)

            cursor.execute(insert_query, data)
            connection.commit()


            ex_id=idGenerator.existing_id
            
            if idGenerator.unique_id != ex_id:
                # ID is unique, insert it into the database
                insert_query = "INSERT INTO user_ids (ttm_id) VALUES (%s)"
                cursor.execute(insert_query, (idGenerator.unique_id,))
                connection.commit()
                print(f"Inserted unique ID: {idGenerator.unique_id}")
                return render_template('display.html',id=idGenerator.unique_id)
            else:
                print(f"ID {idGenerator.unique_id} already exists in the database")
                return render_template('display.html',id="Id has been Generated alrready")
            
        except Exception as e:
            print(e)
            return "Data insertion failed."
        finally:
            cursor.close()
            connection.close()


@app.route('/next-train', methods=['POST'])
def next_train():
    if request.method == 'POST':
        from_place = request.form['from-state']
        to_place = request.form['to-state']
        booking_date = request.form['book-date']
        pnr = request.form['pnr']
        uid=idGenerator.unique_id
        print("\n\n",uid,"\n\n")

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        try:
            # Create a SQL query to insert data
            insert_query = "INSERT INTO train_record_1 (from_place,to_place,booking_date,pnr_number,id) VALUES (%s, %s, %s, %s, %s)"
            data = (from_place,to_place,booking_date,pnr,uid)
            cursor.execute(insert_query, data)
            connection.commit()
            # message = "Data inserted successfully."
            # return render_template('manager-page.html', idm=message)
            return render_template("train-page.html")
        
        except Exception as e:
            print(e)
            return render_template('display.html',id="Data Insertion failed")

        finally:
            cursor.close()
            connection.close()

@app.route('/save-train', methods=['POST'])
def save_train():
    if request.method == 'POST':
        id = request.form['id']
        age = request.form['age']
        train_number = request.form['train-no']
        seat_position = request.form['pos']
        seat_number= request.form['st-no']
        travel_date= request.form['bk-date']
        departure_time= request.form['dep-time']
        departure_station= request.form['dep-station']
        train_type= request.form['type']
        coach_type= request.form['coach_type']
        ticket_price= request.form['price']

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        try:
            # Create a SQL query to insert data
            insert_query = "INSERT INTO train_record_2 (id,age,train_number,seat_position,seat_number,travel_date,departure_time,departure_station,train_type,coach_type,ticket_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (id,age,train_number,seat_position,seat_number,travel_date,departure_time,departure_station,train_type,coach_type,ticket_price)

            cursor.execute(insert_query, data)
            connection.commit()
            message = "Data inserted successfully."
            return render_template('manager-page.html', idm=message) 
        
        except Exception as e:
            print(e)
            return "Data insertion failed."
        finally:
            cursor.close()
            connection.close()

@app.route('/next-bus', methods=['POST'])
def next_bus():
    if request.method == 'POST':
        from_place = request.form['from-state']
        to_place = request.form['to-state']
        booking_date = request.form['book-date']
        transport_service = request.form['transport-service']
        uid=idGenerator.unique_id
        print("\n\n",uid,"\n\n")

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        try:
            # Create a SQL query to insert data
            insert_query = "INSERT INTO bus_record_1 (from_place,to_place,booking_date,transport_service,id) VALUES (%s, %s, %s, %s, %s)"
            data = (from_place,to_place,booking_date,transport_service,uid)

            cursor.execute(insert_query, data)
            connection.commit()
            # message = "Data inserted successfully."
            # return render_template('manager-page.html', idm=message)
            return render_template("bus-page.html")
        
        except Exception as e:
            print(e)
            return render_template('display.html',id="Data Insertion failed")

        finally:
            cursor.close()
            connection.close()

@app.route('/save-bus', methods=['POST'])
def save_bus():
    if request.method == 'POST':
        id = request.form['id']
        age = request.form['age']
        bus_number = request.form['bus-no']
        seat_position = request.form['pos']
        seat_number= request.form['st-no']
        travel_date= request.form['bk-date']
        departure_time= request.form['dep-time']
        departure_place= request.form['dep-place']
        bus_type= request.form['type']
        coach_type= request.form['coach_type']
        ticket_price= request.form['price']

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        try:
            # Create a SQL query to insert data
            insert_query = "INSERT INTO bus_record_2 (id,age,bus_number,seat_position,seat_number,travel_date,departure_time,departure_place,bus_type,coach_type,ticket_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (id,age,bus_number,seat_position,seat_number,travel_date,departure_time,departure_place,bus_type,coach_type,ticket_price)

            cursor.execute(insert_query, data)
            connection.commit()
            message = "Data inserted successfully."
            return render_template('manager-page.html', idm=message) 
        
        except Exception as e:
            print(e)
            return "Data insertion failed."
        finally:
            cursor.close()
            connection.close()


@app.route('/next-flg', methods=['POST'])
def next_flg():
    if request.method == 'POST':
        from_place = request.form['from-state']
        to_place = request.form['to-state']
        booking_date = request.form['book-date']
        pnr = request.form['pnr']
        uid=idGenerator.unique_id

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        try:
            # Create a SQL query to insert data
            insert_query = "INSERT INTO flight_record_1 (from_place,to_place,booking_date,pnr_number,id) VALUES (%s, %s, %s, %s, %s)"
            data = (from_place,to_place,booking_date,pnr,uid)

            cursor.execute(insert_query, data)
            connection.commit()
            # message = "Data inserted successfully."
            # return render_template('manager-page.html', idm=message)
            return render_template("flight-page.html")
        
        except Exception as e:
            print(e)
            return render_template('display.html',id="Data Insertion failed")

        finally:
            cursor.close()
            connection.close()

@app.route('/save-flg', methods=['POST'])
def save_flg():
    if request.method == 'POST':
        id = request.form['id']
        age = request.form['age']
        flight_number = request.form['flg-no']
        cls = request.form['cls']
        seat_number= request.form['st-no']
        travel_date= request.form['bk-date']
        departure_time= request.form['dep-time']
        departure_port= request.form['dep-place']
        flight_type= request.form['type']
        food_option= request.form['food-opt']
        ticket_price= request.form['price']

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        try:
            # Create a SQL query to insert data
            insert_query = "INSERT INTO flight_record_2 (id,age,flight_number,class,seat_number,travel_date,departure_time,departure_port,flight_type,food_option,ticket_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (id,age,flight_number,cls,seat_number,travel_date,departure_time,departure_port,flight_type,food_option,ticket_price)

            cursor.execute(insert_query, data)
            connection.commit()
            message = "Data inserted successfully."
            return render_template('manager-page.html', idm=message) 
        
        except Exception as e:
            print(e)
            return "Data insertion failed."
        finally:
            cursor.close()
            connection.close()
    
# def get_bus_data():
    
    
@app.route('/back')
def back():
    return render_template('index.html')

@app.route('/bus')
def bus():
    return render_template('bus-page.html')

@app.route('/train')
def train():
    return render_template('train-page.html')

@app.route('/flight')
def flight():
    return render_template('flight-page.html')

@app.route('/manager')
def manager():
    return render_template('manager-page.html')

@app.route('/manager-start-bus')
def manager_bus():
    return render_template('manager-busDisplay.html')
@app.route('/manager-start-train')
def manager_train():
    return render_template('manager-trainDisplay.html')
@app.route('/manager-start-flight')
def manager_flight():
    return render_template('manager-flightDisplay.html')

@app.route('/manager-bus',methods=['POST'])
def bus_display():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        travel_id= request.form['travel_id']

        query = "SELECT * FROM bus_record_2 WHERE id = %s ;"
        cursor.execute(query,(travel_id,))
        result = cursor.fetchone()
        # Retrieve the first row of the result
        if result==None:
            return render_template('display.html',id="Data Not Found, Enter Valid Travel Id")
        else:
            age = result[1] if result else None  # Extract the 'age' from the result
            bus_no= result[2]
            seat_pos= result[3]
            seat_no= result[4]
            date=result[5]
            dep_time=result[6]
            dep_place=result[7]
            bus_type=result[8]
            coach_type=result[9]
            ticket_price=result[10]

            query = "SELECT * FROM bus_record_1 WHERE id = %s ;"
            cursor.execute(query,(travel_id,))
            result_data = cursor.fetchone()
            from_place = result_data[0] if result else None  # Extract the 'age' from the result
            to_place= result_data[1]
            booking_date= result_data[2]
            transport_service= result_data[3]

            return render_template('manager-busDisplay.html',age=age,bus=bus_no,seat=seat_pos,sno=seat_no,t_date=date,d_time=dep_time,d_place=dep_place,b_type=bus_type,c_type=coach_type,t_price=ticket_price,tid=travel_id,from_place=from_place,to_place=to_place,bk_date=booking_date,ts=transport_service)

        
        # Return the 'age' as a variable
        re
    except Exception as e:
        print(e)
        return f"Got error {e}"
    finally:
        cursor.close()
        connection.close()


@app.route('/manager-train',methods=['POST'])
def train_display():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        travel_id= request.form['travel_id']
        
        print("\n\n\n\n this is:",travel_id,"\n\n\n")

        query = "SELECT * FROM train_record_2 WHERE id = %s ;"
        cursor.execute(query,(travel_id,))

        result = cursor.fetchone()
        # Retrieve the first row of the result
        if result==None:
            return render_template('display.html',id="Data Not Found, Enter Valid Travel Id")
        else:
            age = result[1] if result else None  # Extract the 'age' from the result
            train_no= result[2]
            seat_pos= result[3]
            seat_no= result[4]
            date=result[5]
            dep_time=result[6]
            dep_place=result[7]
            train_type=result[8]
            coach_type=result[9]
            ticket_price=result[10]

            query = "SELECT * FROM train_record_1 WHERE id = %s ;"
            cursor.execute(query,(travel_id,))
            result_data = cursor.fetchone()
            
            from_place = result_data[0] if result else None  # Extract the 'age' from the result
            to_place= result_data[1]
            booking_date= result_data[2]
            pnr= result_data[3]

            return render_template('manager-trainDisplay.html',age=age,train=train_no,seat=seat_pos,sno=seat_no,t_date=date,d_time=dep_time,d_place=dep_place,t_type=train_type,c_type=coach_type,t_price=ticket_price,tid=travel_id,from_place=from_place,to_place=to_place,bk_date=booking_date,pnr=pnr)

        
        # Return the 'age' as a variable
        re
    except Exception as e:
        print(e)
        return f"Got error {e}"
    finally:
        cursor.close()
        connection.close()




if __name__ == '__main__':
    app.run(debug=True)
