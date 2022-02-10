from App import db, app
from flask_mail import Mail, Message
from flask import Flask
from ..info_mail import email, password

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send')
def send():
    msg = Message('sujet demon mail', sender=email,
            recipients=['theotricot12@gmail.com'])

    msg.html = 'Changer votre mot de passe <button class="pwd_forget"> <a href = "https://www.youtube.com/watch?v=J5bIPtEbS0Q&t=114s"> click here </a> </button>'
    mail.send(msg)
    return "Courrier electronique envoyé"