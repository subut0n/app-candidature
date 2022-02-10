from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash


@app.route('/list_apprenant')
@login_required
def get_list_apprenant():
    """ Admin can display th list of all student
    """
    if current_user.is_admin == True:
        title = ["first_name", "last_name","email_address"]
        return render_template("list_apprenant.html",head="Liste des apprenants",title = title, list_apprenant = Users.query.filter_by(is_admin=False) )
    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page'))