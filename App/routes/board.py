from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/board', methods=['GET','POST'])
@login_required
def board_page():
    """[Allow to generate the template of board.html on board path, if user is authenticated else return on login]

    Returns: 
        [str]: [board page code different if the user is admin or not]
    """
    usercandidacy_attributs = ['company','job_type','date','status']

    if (current_user.is_admin == True):
        return redirect('/board_admin')
    else:
        return render_template('board.html', lenght = len(usercandidacy_attributs), title = usercandidacy_attributs ,user_candidacy=Candidacy.find_by_user_id(current_user.id))
