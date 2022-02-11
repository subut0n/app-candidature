from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from App.utils import isAsciiNumber


@app.route('/candidature', methods= ['GET', 'POST'])
def add_candidature():
    """[Allow to generate the template of add_candidacy.html on candidacy path to add candidacy in the BDD if validate and redirect to the board page when finish]

    Returns:
        [str]: [Candidacy code page]
    """
    form = AddCandidacy()

    def conditions_ok(form):

        if len(form.contact_mobilephone.data) <= 9:
            return False 
        elif isAsciiNumber(form.contact_mobilephone.data) == False:
            return False
        else:
            return True


    if form.validate_on_submit() and conditions_ok(form):
        Candidacy(user_id = current_user.id, company = form.company.data, job_type = form.job_type.data, description = form.description.data, contact_full_name = form.contact_full_name.data, contact_email = form.contact_email.data, contact_mobilephone = form.contact_mobilephone.data, status = form.status.data, comment = form.comment.data, origin = form.origin.data).save_to_db()
        flash('Nouvelle candidature ajouté ', category='success')
        return redirect(url_for('board_page'))
    return render_template('add_candidacy.html', form=form)