from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, Modify_pwd, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash



@app.route('/modify_password/<email>', methods=['GET', 'POST'])
# @login_required
def modify_password(email):
    """[Allow to generate the template of modify_profile.html on modify_profile path to modify profile in the BDD if validate and redirect to the board page when finish]

    Returns:
        [str]: [modify profile code page]
    """
    form = Modify_pwd()
    if form.validate_on_submit():
        current_user.password_hash = generate_password_hash(form.new_password.data, method='sha256')
        db.session.add(current_user)
        db.session.commit()

        flash(f"Votre mot de passe a été modifié",category="success")
        return redirect(url_for('Login_page'))


    return render_template('modify_pwd.html',form=form)