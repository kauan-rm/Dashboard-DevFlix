from app import mail
from flask_mail import Message
from flask import render_template
from config import Config


email = Config()
remetente = email.MAIL_USERNAME
    
def send_email(to, subject, template, **kwargs):
  msg = Message( subject,
  sender=remetente, recipients=[to])
  msg.body = render_template(template + '.html', **kwargs)
  msg.html = render_template(template + '.html', **kwargs)
  mail.send(msg)


  