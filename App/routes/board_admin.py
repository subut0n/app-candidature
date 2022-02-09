from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/board_admin', methods=['GET','POST'])
@login_required
def board_page_admin():
    """[Allow to generate the template of board.html on board path, if user is authenticated else return on login]

    Returns:
        [str]: [board page code different if the user is admin or not]
    """

    admin_candidacy_attributs = ["first_name",'company' ,'date','status']
    
    if (current_user.is_admin == True):  
        return render_template('board_admin.html', lenght = len(admin_candidacy_attributs), title = admin_candidacy_attributs, user_candidacy=Candidacy.get_all_in_list_with_user_name())
    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page'))  