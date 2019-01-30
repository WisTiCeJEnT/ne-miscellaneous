import smtplib
import getpass
import time

def send_by_gmail(recipient,subject,msg,sender_email,sender_password):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,recipient,f"Subject: {subject}\n\n{msg}")
        server.quit()
        print("Email have been sent")
    except:
        print("Error Connecting to Gmail server")
recipient = input("Recipient email: ")
subject = input("Subject: ")
msg = input("Message: ")
sender_email = input("Sender email: ")
sender_password = getpass.getpass()
count = 0
while(True):
    count += 1
    print(msg,count)
    send_by_gmail(recipient,subject,msg,sender_email,sender_password)
    time.sleep(5)
