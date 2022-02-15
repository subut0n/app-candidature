from App import db, app
from flask_mail import Mail, Message
from flask import Flask, request
from ..info_mail import EMAIL_ADDRESS, EMAIL_PASSWORD
import cherrypy

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = EMAIL_ADDRESS
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send_remind/<email>')
def send_remind(email):
    msg = Message('Rappel candidature', sender= EMAIL_ADDRESS,
            recipients=[email])
    varlink = 'http://simploncandidature.herokuapp.com/board'
    
    msg.body = "Vous etes a 7 jours de votre candidature. N'oubliez pas de relancer l'entreprise !"
    mail.send(msg)
    return "Rappel envoyé"