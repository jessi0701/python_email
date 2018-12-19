import smtplib
from email.message import EmailMessage
import getpass
pw = getpass.getpass("sdsdsds")

email_list = ['shrgud7@gmail.com','chhun3830@naver.com']

for email in email_list:
    msg = EmailMessage()
    msg['Subject'] = "title!!"
    msg['From'] = "jessi0701@naver.com"
    msg['To'] = email   #shrgud7@gmail.com, chhun3830@naver.com
    msg.set_content('good')

    smtp_url = 'smtp.naver.com'
    smtp_port = 465
    
    s = smtplib.SMTP_SSL(smtp_url, smtp_port)
    
    s.login('jessi0701',pw)
    s.send_message(msg)