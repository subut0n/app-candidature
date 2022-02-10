from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/job_type')
@login_required
def get_job_type():
    if current_user.is_admin == True:
        comp = [{"job_type" : c.job_type} for c in Candidacy.query.group_by("job_type").all()]
        title = ["job_type"]
        return render_template("list_company.html",head = "Liste des jobs", title = title, list_apprenant=comp)

    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page')) 