from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/status_in_progress')
@login_required
def get_status_in_progress():
    """ liste des apprenant en recherche d'une alternance
    """
    if current_user.is_admin == True:
        choice = "En cours"
        request = Candidacy.query.filter(Candidacy.status == choice).all()
        list_app_id = list(set([request[i].user_id for i in range(0,len(request))]))
        list_app = Users.query.filter(Users.id.in_(list_app_id)).all()
        admin_candidacy_attributs = ["first_name"]
        list_app2 = [app.json() for app in list_app]

        return render_template("list_apprenant.html", head = f"Status : {choice}", title = admin_candidacy_attributs, list_apprenant=list_app2)
    else:
        flash('Vous n\'etes pas un administrateur !',category="danger")
        return redirect(url_for('home_page'))