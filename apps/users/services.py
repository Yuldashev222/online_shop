from django.conf import settings
from django.core.mail import send_mail


def send_email_to_user(email, code):
    send_mail(
        subject='Confirm Email',
        message=f'Your code for enter to online shop: {code}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


