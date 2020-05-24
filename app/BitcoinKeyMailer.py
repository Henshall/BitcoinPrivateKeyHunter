#!/usr/bin/env python3
import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import env

class BitcoinKeyMailer():
    """docstring for BitcoinKeyMailer."""

    def __init__(self):        
        self.text = None   
        
    def setText(self, text):
        self.text = text
        
        
    def generateTextFromArray(self):
        text = ""
        for value in self.data:
            text = text + "----" + value
        return text    
    
    def createMessage(self, text):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = env.SUBJECT
        msg['From'] = email.utils.formataddr((env.SENDERNAME, env.SENDER))
        msg['To'] = env.RECIPIENT
        mimeText = MIMEText(text, 'plain')
        msg.attach(mimeText)
        return msg
        
    def send(self):
        text = self.text
        msg = self.createMessage(text)
        try:  
            server = smtplib.SMTP(env.HOST, env.PORT)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(env.USERNAME_SMTP, env.PASSWORD_SMTP)
            server.sendmail(env.SENDER, env.RECIPIENT, msg.as_string())
            server.close()
        # Display an error message if something goes wrong.
        except Exception as e:
            print ("Error: ", e)
        else:
            print ("Email sent!")
        


# mailer = BitcoinKeyMailer()
# mailer.setEnv(env)
# mailer.setData(["333", "fsfsdf", "wrueyhweir", "jdbfygfusydf", "sdsfsdf", "erw444r"])
# mailer.send()

