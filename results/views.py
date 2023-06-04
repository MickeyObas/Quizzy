from django.shortcuts import render
from django.http import FileResponse

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from quiz.models import UserQuizSession

def gen_pdf(request):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 16)

    lines = [
        "This is line one",
        "This is line one",
        "This is line one",
        "This is line one",
    ]

    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename="Hihi.pdf")