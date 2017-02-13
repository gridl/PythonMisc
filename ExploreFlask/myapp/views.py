# example using the custom decorator in utils.py and the @login_required deocartor

from flask import render_template
from flask_login import login_required

from . import app
from .util import check_expired

@app.route('/use_app')
@login_required
@check_expired
def use_app():
    """ Use our amazing app"""
    return render_template("use_app.html")

@app.route('/account/billing')
@login_required
def account_billing():
    """ Update your billing info"""
    return render_template('account/billing.html')