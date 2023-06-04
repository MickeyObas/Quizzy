from django.dispatch import receiver

from .signals import quiz_completed
from .models import UserQuizSession

@receiver(quiz_completed, sender=UserQuizSession)
def send_result_to_email(sender, **kwargs):
    print(sender)
    print(kwargs)
    pass