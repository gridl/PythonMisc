from flask import Flask, jsonify
import json
import sqlite3
app = Flask(__name__)

@app.route("/api/v1/info")
def home_index():
    conn = sqlite3.connect("vish.db")
    print("Opened database sucessfully")
    api_list = []
    cursor = conn.execute("Select buildtime, version,methods,links from apirelease;")

    for row in cursor:
        a_dict = {}
        a_dict['version'] = row[0]
        a_dict['buildtime'] = row[1]
        a_dict["methods"] = row[2]
        a_dict['links'] = row[3]
        api_list.append(a_dict)
    conn.close()
    return jsonify({'api_version': api_list}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)