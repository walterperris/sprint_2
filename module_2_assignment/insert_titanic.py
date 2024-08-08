import psycopg2
from os import getenv
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from psycopg2.extras import execute_values


DBNAME = getenv('DBNAME')
USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')
PORT = getenv('PORT')

# make our postgres connection and cursor
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT, sslmode='require')
pg_curs = pg_conn.cursor()

def create_table_if_not_exists(cursor):
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS titanic_table (
        Passenger_id SERIAL PRIMARY KEY,
        Survived INT NOT NULL,
        Pclass INT NOT NULL,
        Name VARCHAR(100) NOT NULL,
        Sex VARCHAR(10) NOT NULL,
        Age FLOAT, 
        Siblings_Spouses_Aboard INT NOT NULL,
        Parents_Children_Aboard INT NOT NULL,
        Fare FLOAT NOT NULL
    );
    '''
    cursor.execute(create_table_query)

# Read the CSV
df = pd.read_csv("titanic.csv")

if __name__ == '__main__':
    # Create the table and its associated Schema
    create_table_if_not_exists(pg_curs)

    # Prepare data for insertion
    columns = df.columns.tolist()
    values = df.values.tolist()

    # Construct the insert query
    insert_query = f"""
    INSERT INTO titanic_table ({','.join(columns)})
    VALUES %s;
    """
    
    # Execute the batch insert
    execute_values(pg_curs, insert_query, values)

    pg_conn.commit()
    print("Data inserted successfully!")

    pg_conn.close()