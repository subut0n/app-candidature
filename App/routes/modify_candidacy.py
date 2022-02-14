from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/modify_candidacy', methods=['GET', 'POST'])
@login_required
def modify_candidacy():
    """[Allow to generate the template of modify_candidacy.html on modify_candidacy path to modify candidacy in the BDD if validate and redirect to the board page when finish]

    Returns:
        [str]: [modify candidacy code page]
    """
    form = ModifyCandidacy()
    candidacy_id = request.args.get('id')
    candidacy = Candidacy.query.filter_by(id = candidacy_id).first()

    if form.validate_on_submit():
        
        if candidacy:
            candidacy.job_type = form.job_type.data
            candidacy.description = form.description.data
            candidacy.contact_full_name = form.contact_full_name.data
            candidacy.contact_email = form.contact_email.data
            candidacy.contact_mobilephone = form.contact_mobilephone.data
            candidacy.status = form.status.data
            candidacy.comment = form.comment.data
            candidacy.origin = form.origin.data
            db.session.commit()

            flash(f"La candidature a bien été modifié",category="success")
            return redirect(url_for('board_page'))
        else:
            flash('Something goes wrong',category="danger")
    return render_template('modify_candidacy.html', form=form , candidacy=candidacy.json())