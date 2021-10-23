import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('indexx.html').read_text())
email = EmailMessage()
email['from'] = 'Hogwarts School of Witchcraft and Wizardry'
email['to'] = '###@#.com' #you need to add an email id here to whom you need to send the mail
email['subject'] = 'Partial Horcrux'
#email.set_content('Python here')
email.set_content(html.substitute({'name': 'Harry','namee':'Voldemort'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('#mail', '#pass') #mail-> your mail id #pass->your password
    smtp.send_message(email)
    print('All good Boss!')






