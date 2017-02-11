# authentication decorator



from flask import Flask, render_template
from flask_login import login_required, current_user
from flask_cache import Cache



app = Flask(__name__ , instance_relative_config=True) #To load configuration variables from an instance folder. Use instance folders to keep them out of repo for passwords
app.config.from_object('config') # myapp/config.py
app.config.from_pyfile('config1.py') # From ExploreFlask/instance

#normally include cache configuration settings in this call
cache = Cache(app)



@app.route('/')
@cache.cached(timeout=60)
def index():
    return render_template("index.html")

# only authenticated users will be able to access the /dashboard route
@app.route("/dashboard")
@login_required
def account():
    return render_template("account.html")


if __name__ == "__main__":
    server = '127.0.0.1'
    port = 8080
    app.run(server,port=port)