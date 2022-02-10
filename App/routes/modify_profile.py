from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/modify_profile', methods=['GET', 'POST'])
@login_required
def modify_profile():
    """[Allow to generate the template of modify_profile.html on modify_profile path to modify profile in the BDD if validate and redirect to the board page when finish]

    Returns:
        [str]: [modify profile code page]
    """
    form = ModifyProfile()
    if form.validate_on_submit():
        if current_user.email_address == form.email.data and check_password_hash(current_user.password_hash, form.current_password.data):
            current_user.password_hash = generate_password_hash(form.new_password.data, method='sha256')
            db.session.add(current_user)
            db.session.commit()

            flash(f"Votre mot de passe a été modifié",category="success")
            return redirect(url_for('board_page'))
        else:
            flash('Adresse email ou mot de passe invalide',category="danger")
    return render_template('modify_profile.html',form=form)