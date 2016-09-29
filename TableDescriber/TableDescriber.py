# connects to impala and runs describe on a database
from impala.dbapi import connect
import sys
import re
connection_string = '127.0.0.1'
conn = connect(host=connection_string, port=21050, auth_mechanism="GSSAPI")
cursor = conn.cursor()
dbs = []
dbs = sys.argv[1]
cursor.execute('use ' + str(dbs) + ';')
cursor.execute('show tables;')
tables = cursor.fetchall()
for i in tables:
    clean = re.sub("[(;,')]", '', str(i))
    cursor.execute('describe ' + str(clean) + ';')
    results = cursor.fetchall()
    print("-----------------------------------------------------------------------------")
    print(clean.upper())
    print("-----------------------------------------------------------------------------")
    for j in results:
        cleantable  = re.sub("[(;,')]", ' ', str(j))
        print(cleantable)
