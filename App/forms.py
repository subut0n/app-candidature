from flask_wtf import FlaskForm

from numpy import integer
from wtforms import PasswordField,EmailField,SubmitField,StringField, IntegerField, FieldList, SelectField
from wtforms_alchemy import PhoneNumberField
from wtforms.validators import Length,DataRequired,Email,EqualTo,ValidationError
from .models import Users

class Login(FlaskForm):
    """[Form to login]
    """
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    password = PasswordField(label="Mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Se connecter")


class AddCandidacy(FlaskForm):
    """[Form to add candidacy]
    """
    company = StringField(label='Entreprise', validators=[DataRequired()])
    job_type = StringField(label='Type de poste', validators=[DataRequired()]) #add_candidacy.html a modifier
    contact_full_name = StringField(label='Nom et prénom de votre contact', validators=[DataRequired()])
    contact_email = EmailField(label='Email du contact', validators=[DataRequired()])
    contact_mobilephone = StringField(IntergerField(label='Mobile du contact'))
    status = SelectField('Status', choices=[('En cours', 'En Cours'), ('Annulé', 'Annulé'), ('Refusé', 'Refusé')])
    submit = SubmitField(label='Ajouter une candidature')

class ModifyProfile(FlaskForm):
    """[Form to modify profile]
    """
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    current_password = PasswordField(label="Mot de passe actuel:", validators = [DataRequired()])
    new_password = PasswordField(label="Nouveau mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Valider")

class ModifyCandidacy(FlaskForm):
    """[form to modify candidacy]
    """
    contact_full_name = StringField(label='contact_full_name', validators=[DataRequired()])
    contact_email = StringField(label='contact_email', validators=[DataRequired()])
    contact_mobilephone = StringField(label='contact_mobilephone')
    status = StringField(label='Status', validators=[DataRequired()])

    submit = SubmitField(label="Valider")