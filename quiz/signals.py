from django import dispatch
from django.db.models.signals import post_save

from .models import UserQuizSession

@dispatch.receiver(post_save, sender=UserQuizSession)
def send_result_to_email(sender, instance, created, **kwargs):
    if created:
        pass
    if instance.completed == True:
        correct_ans_container = []
        incorrect_ans_container = []
        user_answer_maps = instance.useranswermap_set.all()
        for u in user_answer_maps:
            if u.is_correct:
                correct_ans_container.append([u.question, u.user_answer])
            else:
                incorrect_ans_container.append([u.question, u.user_answer])



# quiz_completed = dispatch.Signal(providing_args=['quiz_id', 'user'])

