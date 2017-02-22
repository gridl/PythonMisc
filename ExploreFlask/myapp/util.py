from functools import wraps
from datetime import datetime

from flask import flash, redirect, url_for

from flask_login import current_user

def check_expired(func): # when a function is decorated with @check_expired, check_expired() is called and the decorated fucntion is passed as a paramteer
    @wraps(func) # decorator that does some bookkeeping so that decorated_function() appears as func() for purposes of documentaion and debugging
    def decorated_function(*args, **kwargs): # will get all the arguments and kwrgs that were passed to the original view function func()
        if datetime.utcnow() > current_user.account_expires:
            flash("Your account has expired. Update your billing information")
            return redirect(url_for('account_billing'))
        return func(*args, **kwargs) # run the decorated view function func() with its original arguments

    return decorated_function