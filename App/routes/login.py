from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    """[Allow to ask login and generate the template of login.html on login path]

    Returns:
        [str]: [login page code]
    """
    form = Login()
    if form.validate_on_submit():
        user = Users.query.filter_by(email_address=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            if user.is_admin == True:
                flash(f"Vous êtes connecté en tant que : {user.first_name} {user.last_name}, session administrateur",category="success")
            else :
                flash(f"Vous êtes connecté en tant que : {user.first_name} {user.last_name}",category="success")
            return redirect(url_for('board_page'))
        else:
            flash('Adresse email ou mot de passe invalide',category="danger")
    return render_template('login.html',form=form)