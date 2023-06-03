from django.shortcuts import (
    render, 
    get_object_or_404, 
    HttpResponse, 
    redirect
)

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

import random
import json

from quiz.models import Quiz, Question, UserAnswerMap, UserQuizSession
from .utils import process_answer


@login_required(login_url='login')
def index(request):
    quizzes = Quiz.objects.all()

    context = {
        "quizzes": quizzes
    }

    return render(request, "quiz/index.html", context)


@login_required(login_url='login')
def quiz_confirm(request, pk):

    quiz = get_object_or_404(Quiz, id=pk)

    context = {
        "duration": "45 minutes",
        "quiz": quiz
    }

    return render(request, "quiz/quiz_confirm.html", context)

@login_required(login_url='login')
def quiz_session_initiate(request, pk):
    quiz = get_object_or_404(Quiz, id=pk)

    if UserQuizSession.objects.filter(user=request.user, quiz=quiz).exists():
        return HttpResponse("<h3>You have already taken the Quiz.</h3>")

    quiz_session = UserQuizSession.objects.create(user=request.user, quiz=quiz)

    for question in quiz.question_set.all():
        UserAnswerMap.objects.create(question=question, quiz_session=quiz_session)

    return redirect('quiz', pk=quiz.id)

@login_required(login_url='login')
def quiz(request, pk):
    quiz = get_object_or_404(Quiz, id=pk)
    current_user_session = user_session = UserQuizSession.objects.get(user=request.user, quiz=quiz, completed=False)
    current_user_answermaps = UserAnswerMap.objects.filter(quiz_session=current_user_session)
    
    id_questions_unanswered = []
    id_questions_answered = []
    is_last_question = False

    for q in current_user_answermaps:
        if not q.saved:
            id_questions_unanswered.append(q.question.id)
        else:
            id_questions_answered.append(q.question.id)

    try:
        question_id = random.choice(id_questions_unanswered)
        if len(id_questions_unanswered) == 1:
            is_last_question = True
    except:
        question_id = id_questions_answered[-1]
        is_last_question = True

    return redirect(question, pk=question_id, is_last_question=is_last_question)


@login_required(login_url='login')
def question(request, pk=None, is_last_question=None):

    question = Question.objects.get(id=pk)

    context = {
        "question": question,
        "is_last_question": is_last_question
        }

    return render(request, "quiz/question.html", context)

@login_required(login_url='login')
def save_answer(request):

    data = json.loads(request.body)

    question_id = data["question_id"]
    user_answer = data["user_answer"]

    question = Question.objects.get(id=question_id)
    quiz = question.quiz

    user_session = UserQuizSession.objects.get(user=request.user, quiz=quiz, completed=False)

    user_answer_map = UserAnswerMap.objects.get(quiz_session=user_session, question=question)
    user_answer_map.user_answer = user_answer
    user_answer_map.saved = True
    user_answer_map.save()

    return JsonResponse("Completed", safe=False)


@login_required(login_url='login')
def submit_quiz(request):

    if request.method == 'POST':
        score = 0

        user_quiz_session = UserQuizSession.objects.get(user=request.user)

        for u in user_quiz_session.useranswermap_set.all():
            if u.user_answer == u.question.answer:
                score += 1

        user_quiz_session.total_score = score
        user_quiz_session.save()
        user_quiz_session.completed = True
        user_quiz_session.save()

        return redirect('index')

    return render(request, "quiz/submit.html")