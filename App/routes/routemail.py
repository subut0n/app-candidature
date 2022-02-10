from App import db, app
from flask_mail import Mail, Message
from flask import Flask
from ..infoMail import adresseMail, password

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = adresseMail
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send')
def send():
    msg = Message('sujet demon mail', sender='simploncandidature@gmail.com',
            recipients=['a.dzikowski@outlook.fr'])
    
    msg.html = 'Changer votre mot de passe <button class="pwd_forget"> <a href = "https://www.youtube.com/watch?v=J5bIPtEbS0Q&t=114s"> click here </a> </button>'
    mail.send(msg)
    return "message envoyé"