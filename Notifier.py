from email.mime import image
import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

'''
Before working with Telegram’s API, you need to get your own API ID and hash:

https://my.telegram.org/

Login to your Telegram account with the phone number of the developer account to use.
Click under API Development tools.
A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!

'''
api_id = 1234567
api_hash = "bbfbf7d0a685bd0d48faf7bcb8b2abef"

def newsignal(client,message):
    # img=""
    # if message.media:
    #     img = client.download_media(message)
    #This part is commented out...you can use it when a channel contribute pictures and send it but whalealert just spread texts


    #The sender mail address and password
    sender_address = 'notifier@gmail.com'
    sender_pass = '12345678'
    '''
    You should enable 'Less secure app access feature in your sender(notifier) gmail account
    https://myaccount.google.com/lesssecureapps
    '''

    #Reciever Addresses whom do you want to send notification to
    receiver_address = ['abc@gmail.com','def@gmail.com']

    
    #Setup the MIME
    mailmessage = MIMEMultipart()
    mailmessage['From'] = sender_address
    mailmessage['To'] = ", ".join(receiver_address)
    mailmessage['Subject'] = 'Whale Alert New Notification'   #The subject line
    #The body and the attachments for the mail
    print(message.text)
    mailmessage.attach(MIMEText(str(message.text).replace('None','') + "**Follow The Whales At Your Risk**", 'plain'))


    #This part is commented out...you can use it when a channel contribute pictures and send it but whalealert just spread texts
    # if img != "":
    #     with open(img,'rb') as f:
    #         msg_image = MIMEImage(f.read())
    #         mailmessage.attach(msg_image)



    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = mailmessage.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    #This part is commented out...you can use it when a channel contribute pictures and send it but whalealert just spread texts
    # if img:
    #     os.remove(img)


app=Client("Telegram App Name", api_id, api_hash) 


my_handler = MessageHandler(newsignal,filters.channel & filters.chat(-1001309043988))
# '-1001309043988' is whalealert channel id 
app.add_handler(my_handler)
app.run()
