import sqlite3
connection = sqlite3.connect("jeopardy.db")
# print(help(connection))

# get cursor
cursor = connection.cursor()
# print(dir(cursor))
cursor.execute("Select text, answer, value from clue limit 10")
results = cursor.fetchall()
# print(results)
# print(results[0])
print("Example categories: \n")
# for categories in results:
#     print(categories[0])

for clue in results:
    text = clue[0]
    answer = clue[1]
    value = clue[2]

    print("[$%s]" % (value, ))
    print("Question: %s" % (text,))
    print("Answer: What is '%s' ?" % (answer,))
    print("")





connection.close()
