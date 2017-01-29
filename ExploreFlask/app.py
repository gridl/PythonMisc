from flask import Flask

app = Flask(__name__ , instance_relative_config=True) #To load configuration variables from an instance folder. Use instance folders to keep them out of repo for passwords
app.config.from_object('config') # myapp/config.py
app.config.from_pyfile('config1.py') # From ExploreFlask/instance

