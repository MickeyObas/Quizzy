from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail
from django.conf import settings

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    output = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), output)
    if not pdf.err:
        send_mail("Hello", "Hope you are good?", from_email=settings.EMAIL_HOST_USER, recipient_list=['mikhzobby@gmail.com'])
        return HttpResponse(output.getvalue(), content_type='application/pdf')
    return None