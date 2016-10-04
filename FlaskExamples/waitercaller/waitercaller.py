from flask import Flask
from flask import render_template
from flask import request
from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask import redirect # takes a url and creates a response for a route that simply redirects user to the URL
from flask import url_for # builds a URL from a function name
from user import User
from mockdbhelper import MockDBHelper as DBHelper
from flask.ext.login import logout_user
DB= DBHelper()

app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = '3AtAYeEhaE5JODRZh0gBZdvoUKYYGoFdt4l34/W1Ajw0P6FOEb/edDmy3glE7sfcOziGEg4TInxGfw/yGbD9CiIn5VBFuPNDJjJc'

@app.route("/")
def home():
    return render_template("home.html")


# restricted route
@app.route("/account")
@login_required
def account():
    return "You are logged in"


@app.route("/login", methods=['POST'])
def login():
    #load users input into email and password variables
    email = request.form.get("email")
    password = request.form.get("password")
    #load the stored password into user_password variable
    user_password = DB.get_user(email)
    if user_password and user_password == password: # password is returned and password is correct
        user = User(email) # create user object from the email address
        login_user(user, remember=True) #pass user object into flak_login modules login_user
        return redirect(url_for('account')) # create a URL for our account page , pass this into a redirect so user
        # is taken from /login to /account
    return home

@login_manager.user_loader # need ot use this as a decorator that checks the DB to make sure the user exists and
# creates a User object from the identifier we are given. Decorator indicates to Flask_login that this is the
# function we want to use to handle users who already have a cookie assigned and it will pass the user_id variable
# from the cookie to this function whenever user visits the site which already has one
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password: # check if user is in the database
        return User(user_id)


@app.route("/logout")
def logout():
    logout_user() # removes session cookie from the users browser
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(port=5000,debug=True)

