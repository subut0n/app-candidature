from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/candidacy_company')
@login_required
def get_candidacy_company():
    if current_user.is_admin == True:
        comp = request.args.get('company')
        list = Candidacy.query.join(Users).with_entities(Users.last_name,Candidacy.id,Candidacy.company,Candidacy.status,Candidacy.date).filter(Candidacy.company == comp).all()
        afficher = [{"last_name":l.last_name,"status":l.status,"date":l.date,"id":l.id} for l in list]
        title = ["last_name","status","date"]
        return render_template("list_date.html",head = f"Candidature pour l'entreprise : {comp}",title=title,list_apprenant=afficher)
        

    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page'))    