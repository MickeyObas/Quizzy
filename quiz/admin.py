from django.contrib import admin

from .models import Question, Quiz, UserAnswerMap, UserQuizSession

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(UserQuizSession)
admin.site.register(UserAnswerMap)