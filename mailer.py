import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
form email.MIMEBase import MIMEBase
from os.path import basename

def mailer(myval):
    sender_email = "sender's mail"
    receiver_email = "receiver's mail"
    # password = getpass.getpass()
    password = 'password'

    message = MIMEMultipart("alternative")
    message["Subject"] = "Server not working!!"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    try:
        text = """\
        """
        html = """\
        <html>
          <body>
            <p>
               The webserver is not working...please check the attachment for logs
            </p>
          </body>
        </html>
        """.format(myval)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        filepart = MIMEBase('application', 'octet-stream')
        filepart.set_payload(open("response.txt",'rb').read())
        Encoders.encode_base64(filepart)
        message.attach(part1)
        message.attach(part2)
        message.attach(filepart)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
    except e:
        print("Some error ocurred in mailer ! ",e)
    print("Mail sent succesfully!")

myval=input()
mailer(myval)
