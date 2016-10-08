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
from passwordhelper import PasswordHelper
from flask.ext.login import current_user
import config
from bitlyhelper import BitlyHelper

DB= DBHelper()
PH = PasswordHelper()
BH = BitlyHelper() # to use bitly code , create a bitlyhelper object in the main application code

app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = '3AtAYeEhaE5JODRZh0gBZdvoUKYYGoFdt4l34/W1Ajw0P6FOEb/edDmy3glE7sfcOziGEg4TInxGfw/yGbD9CiIn5VBFuPNDJjJc'

@app.route("/")
def home():
    return render_template("home.html")





@app.route("/login", methods=['POST'])
def login():
    #load users input into email and password variables
    email = request.form.get("email")
    password = request.form.get("password")
    #load the stored password into user_password variable
    stored_user = DB.get_user(email)

    if stored_user and PH.validate_password(password, stored_user['salt'], stored_user['hashed']):
        user = User(email)
        login_user(user, remember=True)
        return redirect(url_for('account'))
    return home()


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


@app.route("/register",methods=["POST"])
def register():
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        return redirect(url_for('home'))
    if DB.get_user(email):
        return redirect(url_for('home'))
    salt = PH.get_salt()
    hashed = PH.get_hash(pw1 + salt)
    DB.add_user(email,salt, hashed)
    return redirect(url_for('home'))

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/account")
@login_required
def account():
    tables = DB.get_tables(current_user.get_id())
    return render_template("account.html", tables=tables)

@app.route("/account/createtable",methods=["POST"])
@login_required
def account_createtable():
    tablename = request.form.get("tablenumber")
    # to associate the table with an owner we use the flasklogin current_user functionality to get the current logged
    #  in users ID
    tableid = DB.add_table(tablename, current_user.get_id())
    new_url = BH.shorten_url(config.base_url + "newrequest/" + tableid)
    DB.update_table(tableid, new_url)
    return redirect(url_for('account'))

@app.route("/account/deletetable")
@login_required
def account_deletetable():
    tableid = request.args.get("tableid")
    DB.delete_table(tableid)
    return redirect(url_for('account'))

if __name__ == '__main__':
    app.run(port=5000,debug=True)

