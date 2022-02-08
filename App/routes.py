from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from .models import Users, Candidacy
from .forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from App.utils import isAsciiNumber


@app.route('/')
@app.route('/home')
def home_page():
    """[Allow to generate the template of home.html on home path]

    Returns:
        [str]: [home page code]
    """
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    """[Allow to ask login and generate the template of login.html on login path]

    Returns:
        [str]: [login page code]
    """
    form = Login()
    if form.validate_on_submit():
        user = Users.query.filter_by(email_address=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash(f"Vous êtes connecté en tant que : {user.first_name} {user.last_name}",category="success")
            return redirect(url_for('board_page'))
        else:
            flash('Adresse email ou mot de passe invalide',category="danger")
    return render_template('login.html',form=form)




@app.route('/board', methods=['GET','POST'])
@login_required
def board_page():
    """[Allow to generate the template of board.html on board path, if user is authenticated else return on login]

    Returns: 
        [str]: [board page code different if the user is admin or not]
    """
    admin_candidacy_attributs = ["user_fisrt_name",'company','job_type','date','status']
    usercandidacy_attributs = ['company','job_type','date','status']


    if (current_user.is_admin == True):  
        return render_template('board.html', lenght = len(admin_candidacy_attributs), title = admin_candidacy_attributs, user_candidacy=Candidacy.get_all_in_list_with_user_name())
    else:
        return render_template('board.html', lenght = len(usercandidacy_attributs), title = usercandidacy_attributs ,user_candidacy=Candidacy.find_by_user_id(current_user.id))


@app.route('/logout')
def logout_page():
    """[Allows to disconnect the user and redirect to the home page]
    """
    logout_user()
    flash('Vous êtes correctement déconnecté',category="success")
    return redirect(url_for('home_page'))

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
        Candidacy(user_id = current_user.id, company = form.company.data, job_type = form.job_type.data, description = form.description.data, contact_full_name = form.contact_full_name.data, contact_email = form.contact_email.data, contact_mobilephone = form.contact_mobilephone.data, status = form.status.data, comment = form.comment.data).save_to_db()
        flash('Nouvelle candidature ajouté ', category='success')
        return redirect(url_for('board_page'))
    return render_template('add_candidacy.html', form=form)

@app.route('/modify_profile', methods=['GET', 'POST'])
@login_required
def modify_profile():
    """[Allow to generate the template of modify_profile.html on modify_profile path to modify profile in the BDD if validate and redirect to the board page when finish]

    Returns:
        [str]: [modify profile code page]
    """
    form = ModifyProfile()
    if form.validate_on_submit():
        if current_user.email_address == form.email.data and check_password_hash(current_user.password_hash, form.current_password.data):
            current_user.password_hash = generate_password_hash(form.new_password.data, method='sha256')
            db.session.add(current_user)
            db.session.commit()

            flash(f"Votre mot de passe a été modifié",category="success")
            return redirect(url_for('board_page'))
        else:
            flash('Adresse email ou mot de passe invalide',category="danger")
    return render_template('modify_profile.html',form=form)

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
            db.session.commit()

            flash(f"La candidature a bien été modifié",category="success")
            return redirect(url_for('board_page'))
        else:
            flash('Something goes wrong',category="danger")
    return render_template('modify_candidacy.html', form=form , candidacy=candidacy.json())
    
@app.route('/delete_candidacy')
def delete_candidacy():
    """[Allow to delete candidacy in the BDD with the id and redirect to board page]"""
    
    candidacy_id = request.args.get('id')
    
    Candidacy.query.filter_by(id = candidacy_id).first().delete_from_db()
    flash("Candidature supprimé avec succés",category="success")
    return redirect(url_for('board_page'))


@app.route('/view_apprenant', methods=["GET","POST"])
@login_required
def get_view_apprenant():
    """ Admin can display the profil of a student
    """
    apprenant = request.args.get('apprenant')
    admin_candidacy_attributs = ["first_names",'entreprise','contact_full_name','contact_email', 'contact_mobilephone' ,'date','status']
    apprenant_id = Users.query.filter_by(last_name=apprenant).first().id
    if current_user.is_admin == True:
        return render_template('board.html', lenght = len(admin_candidacy_attributs), title = admin_candidacy_attributs, user_candidacy=Candidacy.find_by_user_id(apprenant_id))
    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page'))

@app.route('/list_apprenant')
@login_required
def get_list_apprenant():
    """ Admin can display th list of all student
    """
    if current_user.is_admin == True:
        title = ["first_name", "last_name","email_address"]
        return render_template("list_apprenant.html",title = title, list_apprenant = Users.query.filter_by(is_admin=False) )
    else:
        flash('You are not an admin',category="danger")
        return redirect(url_for('home_page'))

@app.route('/status_en_cours')
@login_required
def get_status_en_cours():
    """ liste des apprenant en recherche d'une alternance
    
    choix = "En cours"
    admin_candidacy_attributs = ["first_names",'entreprise','contact_full_name','contact_email', 'contact_mobilephone' ,'date','status']
    if current_user.is_admin == True:
        apprenant_id = []
        for name in Users.query.all():
            if choix not in Candidacy.find_by_user_id(name.id):
                apprenant_id.append(name.id)
        return render_template("board.html",title = admin_candidacy_attributs, user_candidacy=Users.query.filter_by())
    """
    pass

@app.route('/board/details')
def show_candidacy_details():
    candidacy_id = request.args.get('id')
    candidacy = Candidacy.query.filter_by(id=candidacy_id).first()
    return render_template('candidacy_details.html', candidacy=candidacy.json())