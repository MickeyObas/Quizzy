from django.urls import path

from . import views

urlpatterns = [
    path("", views.gen_pdf, name="gen_pdf")
]