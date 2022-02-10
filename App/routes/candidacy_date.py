from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/candidacy_date')
@login_required
def get_candidacy_date():
    if current_user.is_admin == True:
        #user_candidacy=Candidacy.get_all_in_list_with_user_name()
        #u = user_candidacy.querry.oder_by("date")
        return redirect(url_for('home_page')) 
        
    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page'))