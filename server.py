import sqlite3, os
from dotenv import load_dotenv
# from flask_mail import Mail, Message

from service import db, create_app, models

load_dotenv()
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

def main():
  app = create_app()
  db.create_all(app)
  app.run(debug=True, host=HOST, port=PORT)

if __name__ == '__main__':
  main()







# recipient = 'fedoravdeev3@gmail.com'
# ADMIN = os.getenv('ADMIN')
# mail = Mail(app)
# def send_email(subject, sender, recipients, text_body, html_body):
#   msg = Message(subject, sender=sender, recipients=recipients)
#   msg.body = text_body
#   msg.html = html_body
#   test = mail.send(msg)
#   print(test, '2')
# send_email('Testim', ADMIN, [recipient], 'text body', '<h1>HTML body</h1>')
