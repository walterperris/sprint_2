# Step 0 - Imports
import sqlite3
import queries as q

# step 1 - Connect to the databasw
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - Create a cursor
cursor = connection.cursor()

# step 3 - Write a query
# (See the queries.py file)   
#query = 'SELECT character_id, name FROM charactercreator_character;'

# step 4 - Execute the query on the cursor and fetch the results
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])


# step 5 - Print the results
#for result in results:
#    print(result)

# step 6 - Close the connection
#connection.close()