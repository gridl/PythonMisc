import sqlite3
connection = sqlite3.connect("jeopardy.db")
# print(help(connection))

# get cursor
cursor = connection.cursor()
# print(dir(cursor))
cursor.execute("Select game from Category order by random() limit 1")
results = cursor.fetchall()
# print(results)
# print(results[0])
game_id = results[0][0]
print("Categories for game #%d: " %(game_id,))

query = """Select name, round from category where game = %d order by round """ % (game_id,)

cursor.execute(query)
results = cursor.fetchall()





connection.close()
