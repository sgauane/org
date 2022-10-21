import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class UtilEmail:

    MY_ADDRESS = "sgauaneat@gmail.com"
    PASSWORD = "ijwbfiefjzrhzpyi"

    def send(self):
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(self.MY_ADDRESS, self.PASSWORD)

        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        # message = message_template.substitute(PERSON_NAME=name.title())
        message = "Teste"

        # setup the parameters of the message
        msg['From'] = self.MY_ADDRESS
        msg['To'] = "samgaus87@gmail.com"
        msg['Subject'] = "This is TEST"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)

        del msg