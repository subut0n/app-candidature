from App import db, app
from flask_mail import Mail, Message
from flask import Flask, request
from ..infoMail import EMAIL_ADDRESS, EMAIL_PASSWORD
import cherrypy

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = EMAIL_ADDRESS
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send/<email>')
def send(email):
    msg = Message('sujet demon mail', sender= EMAIL_ADDRESS,
            recipients=[email])
    varlink = 'http://127.0.0.1:5000/modify_password/' + email
    
    msg.body = "Changer votre mot de passe \n http://127.0.0.1:5000/modify_password/" + email
    mail.send(msg)
    return "message envoyé"
