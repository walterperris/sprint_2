
import sqlite3
import queries as q
import pandas as pd


# DB Connect function
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    # Make the cursor
    curs = conn.cursor()
    # Execute the query
    curs.execute(query)
    # Pull/Return the results
    return curs.fetchall()

if __name__ == '__main__':
    conn = connect_to_db()
    #print(execute_q(conn, q.SELECT_ALL)[:5])
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER)
    df = pd.DataFrame(results)
    df.columns = ['name', 'avg_item_weight']
    df.to_csv('rpg_db.csv', index = False)
    print(df.head())
    conn.close()    

