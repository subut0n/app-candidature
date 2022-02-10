from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/redirect_to')
@login_required
def redirect_to():
    page = request.args.get('page')
    if current_user.is_admin == True:
        if page == "status":
            
            return redirect(url_for('get_status_in_progress'))
        elif page == "first_name":
            return redirect(url_for("get_list_apprenant")) 
        elif page == "company":
            return redirect(url_for("get_company"))
        elif page == "job_type":
            return redirect(url_for("get_job_type"))
        elif page =="date":
            return redirect(url_for("get_candidacy_date"))
        else:
            return render_template('home.html') 

    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page'))  