import smtplib
from email.message import EmailMessage
import csv
import getpass
pw = getpass.getpass("sdsdsds")

f = open('e.csv','r',encoding='utf=8')

read_csv = csv.reader(f)
smtp_url = 'smtp.naver.com'
smtp_port = 465
    
s = smtplib.SMTP_SSL(smtp_url, smtp_port)
s.login('jessi0701',pw)


for email in read_csv:
    msg = EmailMessage()
    msg['Subject'] = email[0]+'에게...'
    msg['From'] = "jessi0701@naver.com"
    msg['To'] = email[1]   #shrgud7@gmail.com, chhun3830@naver.com
    msg.set_content('안뇽')
    s.send_message(msg)
    
    
f.close()