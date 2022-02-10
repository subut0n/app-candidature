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
        user_candidacy = Candidacy.query.join(Users).with_entities(Users.first_name,Candidacy.id, Candidacy.company, Candidacy.contact_full_name,Candidacy.date,Candidacy.status).order_by(Candidacy.date.desc()).all()
        affichage = [{"first_name":c.first_name,"date":c.date,"company":c.company,"id":c.id} for c in user_candidacy]
        title = ["first_name","company","date"]
        return render_template("list_date.html",head = "Candidatures par date",title=title,list_apprenant=affichage) 
        
    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page'))  