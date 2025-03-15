from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string


@shared_task
def send_order_email(user_email, context, template_prefix):
    subject = render_to_string(f'email/{template_prefix}_subject.txt', context)
    body = render_to_string(f'email/{template_prefix}_body.txt', context)
    send_mail(
        subject.strip(),
        body,
        'noreply@eastafricom.com',
        [user_email],
        fail_silently=False,
    )
# This is a Celery task that sends an email. It uses Django's send_mail
# function to send an email to a user. The email subject and body are rendered
# using Django's render_to_string function. The template_prefix argument is
# used to determine which email template to use. The task is decorated with
# @shared_task to make it a Celery task.
