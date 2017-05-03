import sqlite3

db_filename = 'todo.db'

# Connection objects have a row_factory property that allows the calling code to control the type of object created to represent each row in the query result set.
with sqlite3.connect(db_filename) as conn:
    #Change the row factory to use Row
    conn.row_factory =sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(""" select name,description, deadline from project where name = 'pymotw' """)
    name,description, deadline = cursor.fetchone()

    print('Project details for {} ({}) \n due {}'.format(description,name,deadline))
    cursor.execute(""" select id,priority, status, deadline, details from task where project = 'pymotw'  order by deadline """)


    print('\n Next 5 tasks')

    for row in cursor.fetchmany(5):
        print('{:2d} [{:d}] {:>25} [{:<8}] ({})'.format(row['id'], row['priority'], row['details'], row['status'], row['deadline']))
