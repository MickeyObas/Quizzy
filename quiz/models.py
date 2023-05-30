from django.db import models

from accounts.models import CustomUser

class Quiz(models.Model):
    title = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.title
    
    @property
    def questions_count(self):
        return self.question_set.all.count()
    

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    option_1 = models.CharField(max_length=256, blank=True, null=True)
    option_2 = models.CharField(max_length=256, blank=True, null=True)
    option_3 = models.CharField(max_length=256, blank=True, null=True)
    option_4 = models.CharField(max_length=256, blank=True, null=True)
    answer = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        if len(self.content) <= 20:
            return self.content
        return self.content[:16] + "...?"
    

class UserQuizSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'UserQuizSessions'

    def __str__(self):
        return f"User: {self.user.email}, Quiz: {self.quiz}"


class UserAnswerMap(models.Model):
    quiz_session = models.ForeignKey(UserQuizSession, on_delete=models.CASCADE)
    question =  models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=256, null=True)
    is_correct = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'UserAnswerMaps'
    
    def __str__(self):
        return f"User {self.quiz_session.user.email} picked option '{self.user_answer}'"





