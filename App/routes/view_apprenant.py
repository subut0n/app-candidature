from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/view_apprenant', methods=["GET","POST"])
@login_required
def get_view_apprenant():
    """ Admin can display the profil of a student
    """
    apprenant = request.args.get('apprenant')
    admin_candidacy_attributs = ["first_names",'company' ,'date','status']
    apprenant_id = Users.query.filter_by(last_name=apprenant).first().id
    if current_user.is_admin == True:
        return render_template('board.html', lenght = len(admin_candidacy_attributs), title = admin_candidacy_attributs, user_candidacy=Candidacy.find_by_user_id(apprenant_id))
    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page'))