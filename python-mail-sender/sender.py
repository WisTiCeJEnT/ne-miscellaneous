import smtplib
import getpass

def send_by_gmail(recipient,subject,msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        sender_email = input("Sender email: ")
        sender_password = getpass.getpass()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,recipient,f"Subject: {subject}\n\n{msg}")
        server.quit()
        print("Email have been sent")
    except:
        print("Error Connecting to Gmail server")
send_by_gmail(input("Recipient email: "),input("Subject: "),input("Message: "))
