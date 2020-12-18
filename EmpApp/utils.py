import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Util:
    @staticmethod
    def sendMail(data):

        message = Mail(
            from_email='info@engagenreap.com',
            to_emails=[data['to_email']],
            subject=data['email_subject'],
            html_content=data['email_body']
        )
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
