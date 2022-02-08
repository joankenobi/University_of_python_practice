# Practicing postgresql

[Direccion del curso](https://drive.google.com/drive/folders/19AaxGSa2GnOMw6o4j9L5jsmd5lQRzb8R)

## Installations <a id="A"></a>

- [X] Install PostgreSQL in Linux.

I only run this code in the terminal of linux_mint_20:

``` bash
 $sudo apt install postgresql postgresql-contrib
```

- [X] create a database and practice.

For this I used an extension for VS Code called **MySQL** by Cweija, this extension can connect with PostgreSQL and I used it because I can't use Pgadmin in **Linux mint**.

[MySQL for VS Code](https://img.shields.io/endpoint?color=orange&label=joan&logo=facebook&logoColor=red&style=flat-square&url=joan%3A%20https%3A%2F%2Fshields.io%2Fendpoint)

In Python, I use **psycopg2** module installed with Conda.

``` bash
    $conda install psycopg2
```

- [X] create a table.

For create a table apply 

```python

    sentence= CREATE TABLE table_name (
        column1 datatype constraints (restricciones),
        column2 datatype constraints,
        column3 datatype constraints,
    ) 

    connection.cursor.execute(sentence)

```
## Create table

```python
import psycopg2 as bd

connection= bd.connect(user="postgres", password="warc", host="127.0.0.1", port="5432", database="name")
date=dtime.date.today()

try:
    with connection:
        with connection.cursor() as cursor:
            #the constraint "serial" in like index
            sentencia= """CREATE TABLE persons2 (person_id serial, 
            name varchar(255) NOT NULL, 
            last_name varchar(255) NOT NULL, 
            mail varchar(255) UNIQUE)"""
            cursor.execute(sentencia)
            
except Exception as e:
    print(f"Ocurre el siguiente error: {e}")

finally:
    connection.close()
```

## Multiples inserts in table db <a id="B"></a>

For the insert various values, we need to apply the `executemany(sentence, values)` opposite to a single value insert, where I used `execute(sentence, values)` this is the practice code:

```python

import psycopg2 as bd
import datetime as dtime


conexion= bd.connect(user="postgres", password="warc", host="127.0.0.1", port="5432", database="name")

try:
    with conexion:
        with conexion.cursor() as cursor:
            date=dtime.date.today()
            sentencia= "INSERT INTO test2(create_time, columntest2) VALUES(%s, %s)"
            valores=((date, "joan2"),(date, "joel2"),(date, "Josue2"))
            cursor.executemany(sentencia,valores)
            registros_saved=cursor.rowcount

except Exception as e:
    print(f"Ocurre el siguiente error: {e}")

finally:
    conexion.close()    


if __name__=="__main__":
    print(date)
```

The order of the table(attributes) called `test2(create_time, columntest2)` continue the sequence in `VALUES(%s, %s)` respectively, the same apply in `valores=((date, "joan2"),(date, "joel2"),(date, "Josue2"))` where the first one item `(date, "joan2")` set in `VALUES(%s, %s)` respectively, the same with others one's items.

## Multiples SELECTS data in table db <a id="C"></a>

From **Video 5**

For this practice I use in the code `cursor.fetchall()` since `cursor.rowcount`.

- `cursor.fetchall()` for select multiple data.
- `cursor.fetchone()` for select one data.

```python
    conexion= bd.connect(user="postgres", password="warc", host="127.0.0.1", port="5432", database="name")

    try:
        with conexion:
            with conexion.cursor() as cursor:
                date=dtime.date.today()
                sentencia= "SELECT * FROM test2 WHERE id IN %s "
                values=((2,3),)
                cursor.execute(sentencia,values)
                registros_saved=cursor.fetchall()
                for reg in registros_saved:
                 print(reg)

    except Exception as e:
        print(f"Ocurre el siguiente error: {e}")

    finally:
        conexion.close()    
```

## UPDATE multiples registers

For this code, I'm going to update multiple registers in a data base, for varius registers you need to use `cursor.executemany()` and for one register apply `cursor.execute()`.

```python

import psycopg2 as bd
import datetime as dtime

connection= bd.connect(user="postgres", password="warc", host="127.0.0.1", port="5432", database="name")
date=dtime.date.today()

try:
    with connection:
        with connection.cursor() as cursor:
            date=dtime.date.today()
            #With UPDATE you do not use INTO you apply SET
            sentencia= "UPDATE test2 SET create_time= %s WHERE id=%s "
            values=(
                (date,7),
                (date,5),
                (date,6)
                )
            cursor.executemany(sentencia,values)
            #Cursor.rowcount retorna cuantos cambios se han realizado por fila?
            registers_update=cursor.rowcount
            print(registers_update)

except Exception as e:
    print(f"Ocurre el siguiente error: {e}")

finally:
    connection.close()    
```

## DELETE multiples registers

For `DELETE` you do use `cursor.execute()` with **single or various** Deletes.

```python

    try:
    with connection:
        with connection.cursor() as cursor:
            date=dtime.date.today()
            sentencia= "DELETE FROM test2 WHERE id IN %s "
            dato_ingresado=input("ingrese datos separados por coma: ")
            values=(tuple(dato_ingresado.split(",")),)
            #executemany not fun
            cursor.execute(sentencia,values)
            #cursor.rowcount retorna cuantos cambios se han realizado por fila?
            registers_update=cursor.rowcount
            print(registers_update)

except Exception as e:
    print(f"Ocurre el siguiente error: {e}")

finally:
    connection.close()

```

## Reading of SQL code <a id="L"></a>

- `"INSERT INTO test2(create_time, columntest2) VALUES(%s, %s)"`
  
  INSERT (funtion) INTO (into) test2(create_time **(column 1)** , columntest2 **(column 2)**) (Columns of table and his order) VALUES(%s **(in column 1)** , %s **(in column 2)**) (values and his order in row)

- `"SELECT * FROM test2 WHERE id >= 5"`
  
  SELECT (funtion) * (all?) FROM (from) test2 (table) WHERE (condition) id (column) >= (Comparer) 5

- `"UPDATE test2 SET create_time= %s WHERE id=%s"`
  
  UPDATE (Overwriting) test2 (tabla) SET (columns seting) create_time (column)= %s (value) WHERE (condition) id (column) =%s (value) "

- `"DELETE FROM test2 WHERE id IN %s "`
  
  DELETE (funtion) FROM (from) test2 (tabla) WHERE (condition) id IN (iterar) %s

## Some notes <a id="N"></a>

### Every time, add the values in the `execute(sentence, values)` when you have it

Example:

sentencia= "SELECT * FROM test2 WHERE id IN `%s` "

`values`=((2,3),) *All values need a tuple of tuples* IMPORTANT

cursor.execute(sentencia,`values`)

### Always need close de conexion and conexion.cursor

- Use this code to create the conexion.cursor and close it
  
    ```python
      with conexion:
                with conexion.cursor() as cursor:
    ```

- For close the conection use this in the end of conexion process

    ```python
      finally:
            conexion.close()
    ```