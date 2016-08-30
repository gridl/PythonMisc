import sqlite3
connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("Select game from Category order by random() limit 1")
results = cursor.fetchall()

category_id,name = results[0]
print(name)


query = """select text, answer , value from Clue where category=%s order by value """ %(category_id)

cursor.execute(query)
results = cursor.fetchall()

for clue in results:
    text, answer, value = clue
    print("[$%s]") %(value,)
    print("Question: %s" %(text,))
    print("Answer: What is %s ?" %(answer,))
    print("")
