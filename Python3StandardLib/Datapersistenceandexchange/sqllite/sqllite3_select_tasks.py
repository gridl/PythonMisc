import sqlite3


db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select  id,priority,details,status,deadline from task where project = 'pymotw'
    """)

    for row in cursor.fetchall():
        task_id,priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(task_id, priority, details, status, deadline))

        # return value is a sequence of tuples containing the values for the columns included in the select clause of the query

