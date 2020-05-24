#!/usr/bin/env python3
import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class BitcoinKeyMailer():
    """docstring for BitcoinKeyMailer."""

    def __init__(self):        
        self.env = None
        self.text = None   
        
    def setText(self, text):
        self.text = text
        
    def setEnv(self, env):
        self.env = env
        
    def generateTextFromArray(self):
        text = ""
        for value in self.data:
            text = text + "----" + value
        return text    
    
    def createMessage(self, text):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.env.SUBJECT
        msg['From'] = email.utils.formataddr((self.env.SENDERNAME, self.env.SENDER))
        msg['To'] = self.env.RECIPIENT
        mimeText = MIMEText(text, 'plain')
        msg.attach(mimeText)
        return msg
        
    def send(self):
        text = self.text
        msg = self.createMessage(text)
        try:  
            server = smtplib.SMTP(self.env.HOST, self.env.PORT)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.env.USERNAME_SMTP, self.env.PASSWORD_SMTP)
            server.sendmail(self.env.SENDER, self.env.RECIPIENT, msg.as_string())
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

