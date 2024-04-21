from django.core.mail import send_mail
from django.conf import settings


def send_order_email():
    send_mail(
        'Проверка',
        f'да',
        settings.EMAIL_HOST_USER,
        ['frogugly@yndex.ru'],
        fail_silently=False,

    )
