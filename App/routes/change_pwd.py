from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Forgotten_pwd, Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from App.utils import list_mail

@app.route('/new_password', methods=['GET', 'POST'])
def new_password():
    """[Allow to ask login and generate the template of login.html on login path]

    Returns:
        [str]: [login page code]
    """
    form = Forgotten_pwd()
    if form.validate_on_submit() and form.email.data in list_mail:
        emailuser = form.email.data
        user = Users.query.filter_by(email_address=form.email.data).first()
        return redirect(url_for('send', email = emailuser))
 
    else:
        flash('Adresse email invalide',category="danger")
    return render_template('new_pwd.html',form=form)