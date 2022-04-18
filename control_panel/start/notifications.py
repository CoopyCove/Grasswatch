from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


#user information is passed through request
#title and body are strings
#att is the an image object
def notify(request, title="Default title", body="Default body", att=None):
    template = render_to_string('start/email_notification.html', {'name': request.user.first_name, 'body':body })
    email = EmailMessage(
        title,
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    email.fail_silently = False
    if att:
        email.attach(att.image.name, att.image.read())
    email.send()

#my mess
def notify2(request, title="Default title", body="Default body", att=None):
    
    context = {
    'first_name': request.user.first_name,
    'img_name' : att.name,
    'img_results': att.results,
    'img_date' : att.date,
    'body': body,
    }
    
    template = render_to_string('start/email_notification.html', context)
    email = EmailMessage(
        subject = title,#The subject line of the email.
        body = template,#The body text. This should be a plain text message.
        from_email = settings.EMAIL_HOST_USER,#From. The sender’s address.
        to = [request.user.email],#To. A list or tuple of recipient addresses.    
    )
    email.content_subtype = "html"  # Main content is now text/html
    email.fail_silently = False
    if att:
        email.attach(att.image.name, att.image.read())
    email.send()

