from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/company')
@login_required
def get_company():
    if current_user.is_admin == True:
        #comp = [{"company" : c.company} for c in Candidacy.query.with_entities(Candidacy.company).distinct()]
        comp = [{"company" : c.company} for c in Candidacy.query.group_by(Candidacy.company).with_entities(Candidacy.company)]
        title = ["company"]
        return render_template("list_company.html",head = "Liste des entreprises", title = title, list_apprenant=comp)

    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page')) 