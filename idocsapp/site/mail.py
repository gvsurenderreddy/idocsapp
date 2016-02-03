from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.conf import settings


def send_mail_template(subject, template_name, context, recipient_list, from_email=settings.DEFAULT_FROM_EMAIL,
                       fail_silently=False):
    message_html = render_to_string(template_name, context)
    message_txt = striptags(message_html)

    attach = context['attach']

    email = EmailMultiAlternatives(subject=subject, body=message_txt, from_email=from_email, to=recipient_list)

    if attach is None:
        email.attach_alternative(message_html, "text/html")
        email.send(fail_silently=fail_silently)
    else:
        email.attach(attach.name, attach.read(), attach.content_type)
        email.attach_alternative(message_html, "text/html")
        email.send(fail_silently=fail_silently)
