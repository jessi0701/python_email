import smtplib
from email.message import EmailMessage
import getpass
pw = getpass.getpass("sdsdsds")




msg = EmailMessage()
msg['Subject'] = "title!!"
msg['From'] = "jessi0701@naver.com"
msg['To'] ="chhun3830@naver.com"  
#msg.set_content('good')

msg.add_alternative('''
<h1> Hi!! </h1>
<p> i'm nokhyeong</p>
''',subtype="html")

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)

s.login('jessi0701',pw)
s.send_message(msg)