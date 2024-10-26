from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'Sender Email/your mailid'
email_password = 'password' # Generate your password >google ACC> three step verification success > app password > Generate your password

email_receiver = 'Recerivers Email'

subject = 'congratulation on finishing Email Sender on python'
body = '''
If you recived this message, you are one step closer to you goal
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content = body

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


