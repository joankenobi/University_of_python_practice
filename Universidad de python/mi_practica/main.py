import psycopg2 as bd
import datetime as dtime

connection= bd.connect(user="postgres", password="warc", host="127.0.0.1", port="5432", database="name")
date=dtime.date.today()

try:
    with connection:
        with connection.cursor() as cursor:
            sentencia= """CREATE TABLE persons2 (person_id serial, 
            name varchar(255) NOT NULL, 
            last_name varchar(255) NOT NULL, 
            mail varchar(255) UNIQUE)"""
            cursor.execute(sentencia)
            
except Exception as e:
    print(f"Ocurre el siguiente error: {e}")

finally:
    connection.close()    