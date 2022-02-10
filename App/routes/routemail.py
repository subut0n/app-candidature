from App import db, app
from flask_mail import Mail, Message
from flask import Flask

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = EMAIL_ADDRESS
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send')
def send():
    msg = Message('sujet demon mail', sender=email,
            recipients=['theotrc12@gmail.com']) #email temporaire

    msg.html = 'Changer votre mot de passe <button class="pwd_forget"> <a href = "https://www.youtube.com/watch?v=J5bIPtEbS0Q&t=114s"> click here </a> </button>'
    mail.send(msg)
    return "Courrier electronique envoyé"