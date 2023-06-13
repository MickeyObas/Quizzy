from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("confirm/<int:pk>", views.quiz_confirm, name="confirm"),
    path("initiate/<int:pk>", views.quiz_session_initiate, name="quiz_session_initiate"),
    
    path("quiz/<int:pk>", views.quiz, name="quiz"),
    path("question/<int:pk>/<is_last_question>", views.question, name="question"),
    
    path("save_answer", views.save_answer, name="save_answer"),
    path("submit", views.submit_quiz, name="submit"),
]