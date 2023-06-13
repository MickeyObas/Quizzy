from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

from django.shortcuts import render
from django.template.loader import render_to_string

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from quiz.models import Quiz, UserQuizSession

import random

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    output = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), output)
    pdf = output.getvalue()
    if pdf is not None:
        return pdf
    return None


def generate_send_pdf(request, *args, **kwargs):

    quiz_session = UserQuizSession.objects.get(user=request.user)
    quiz = quiz_session.quiz
    user_answer_maps = quiz_session.useranswermap_set.all()

    print(quiz.title)
    
    context = {
        "quiz": quiz,
        "total_questions": quiz.questions_count,
        "score": quiz_session.total_score,
        "user_answer_maps": user_answer_maps
    }

    pdf = render_to_pdf("result.html", context)

    if pdf:

        filename = 'Result' + request.user.email + str(random.randint(1, 1000)) + '.pdf'
        mail_subject = 'Results Notification'
        message = render_to_string('result_message.html', {
            "user": request.user,
            "quiz": quiz
        })

        email = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, to=[''.format(quiz_session.user.email)])
        email.attach(filename, pdf, 'application/pdf')
        email.send(fail_silently=False)

    