
import json

movie_json = """
{
"Title" : "Fast and the furious",
"year" : "2016",
"Runtime": "113 min",
"Country": "USA"
}
"""

print(type(movie_json), movie_json)

md = {

"Title" : "Fast and the furious",
"year" : "2016",
"Runtime": "113 min",
"Country": "USA"

}

print(type(md),md)

#Turn string dynamically into json at runtime

movie_data = json.loads(movie_json)
print(type(movie_data),movie_data)

print("the title is {}".format(movie_data.get('Title')))

#back to string to save on a file system
movie_json_text_2 = json.dumps(movie_data)
print(type(movie_json_text_2),movie_json_text_2)