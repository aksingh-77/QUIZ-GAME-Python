import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from re import *
import datetime

def confirmationMail(mail,code,otp):
    e_from='EXAMPLE@gmail.com'
    t=mail

    msg = MIMEMultipart()
    msg['From']=e_from
    msg['To']=t
    msg['Subject']='Email Confirmation'

    if(code==1):
        name=match(r'^.+@',mail).group().replace('@','').strip()
        message='''Welcome  {0}
We are glad to make you the player of this Game
For Email Confirmation just
Use this OTP  -    {1}
This Email Was Generated on  {2} '''.format(name,otp,datetime.datetime.now())
        body = message
        msg.attach(MIMEText(body, 'plain'))
    elif(code>1):
        name=match(r'^.+@',mail).group().replace('@','').strip()
        message='''Hello {0}
Your Scored  {1} Points
Answers Review {2}
This Email Was Generated on  {3} '''.format(name,code,otp,datetime.datetime.now())
        body = message
        msg.attach(MIMEText(body, 'plain'))
        
    
    server=smtplib.SMTP('SMTP.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(enter your mail here,'PASSWORD_FOR_MAILID')
    server.ehlo()

    text = msg.as_string()
    server.sendmail(e_from,t,text)
    server.close()
