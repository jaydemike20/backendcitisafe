from templated_mail.mail import BaseEmailMessage

class ConfirmationEmail(BaseEmailMessage):
    template_name = "email/confirmation.html"
