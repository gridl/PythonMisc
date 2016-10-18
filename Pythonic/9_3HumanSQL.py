import os
import records
db_file = os.path.join(os.path.dirname(__file__),'demo_db_sqlite')
conn_str = 'sqllite:///' + db_file

db.records.Dabase(conn_str)
rows = db.query("Select  * from measurement where value > .9 order by value desc")

for r in rows[:5]:
    print(r)




