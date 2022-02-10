from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/board/details', methods=["GET","POST"])
@login_required
def show_candidacy_details():
    candidacy_id = request.args.get('id')
    candidacy = Candidacy.query.filter_by(id=candidacy_id).first()
    return render_template('candidacy_details.html', candidacy=candidacy.json())