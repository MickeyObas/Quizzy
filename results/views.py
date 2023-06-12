from django.shortcuts import render
from django.http import FileResponse

import io
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from .utils import render_to_pdf

from quiz.models import UserQuizSession

# def gen_pdf(request):
#     buffer = io.BytesIO()
#     c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
#     textobj = c.beginText()
#     textobj.setTextOrigin(inch, inch)
#     textobj.setFont("Helvetica", 16)

#     lines = [
#         "This is line one",
#         "This is line one",
#         "This is line one",
#         "This is line one",
#     ]

#     for line in lines:
#         textobj.textLine(line)

#     c.drawText(textobj)
#     c.showPage()
#     c.save()
#     buffer.seek(0)

#     return FileResponse(buffer, as_attachment=True, filename="Hihi.pdf")

def generate_pdf(request, *args, **kwargs):
    
    context = {
        "result": "123",
        "score": "15",
        "status": "Good"
    }

    pdf = render_to_pdf("result.html", context)

    if pdf:
        return HttpResponse(pdf, content_type="application/pdf")
    return HttpResponse("Not Found")