import psycopg2
from postgress import config
import csv

def create_tables():
    """ create tables in the PostgreSQL database"""
    command = """
        CREATE TABLE Customers (
            CustomerId Integer PRIMARY KEY,
            Name varchar(200),
            Age Integer NOT NULL,
            Street varchar(200),
            City varchar(100),
            State varchar(100),
            Zip varchar(30)
        )
        """

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()





def insert_Customers_list(customer_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO Customers(customerid, name, age, street, city, state, zip) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement

        cur.execute(sql, customer_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insertfromcsv(file):
    try:

        with open('Data/CSV/Datagen.CSV','r') as f:  # Instead of using the open comand directly use with open, this will help us in avoiding closing the reader manually also there are other benifits
            myreader = csv.reader(f)  # DictReader will help us in reading each cell of data with name. Instead of calling row[1] we can say row['Name']. This allow better readability.
            headers = next(myreader)
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement

            cur.execute('select name from customers')
            names = cur.fetchall()

            names = [name[0] for name in names]

            for i, row in enumerate(myreader):
                print(i)
                if row[1] not in names:
                    insert_Customers_list(row)
                    print("{} inserted".format(row[1]))
                else:
                    print(f'{row[1]} already exists in database')
    except Exception as error:
        print(error)



if __name__ == '__main__':
    create_tables()
