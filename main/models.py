from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default=' ')
    created_at = models.DateTimeField(auto_now_add=True)
    times_taken = models.IntegerField(default=0, editable=False)

    @property
    def question_count(self):
        return self.question_count()
    
    class Meta():
        verbose_name_plural = "Quizzes"
        ordering = ['id']

    def __str__(self):
        return self.title

class Questions(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        related_name = "answers",
        on_delete=models.DO_NOTHING
    )
class Answer(models.Model):
    questions = models.ForeignKey(
        Questions,
        related_name='answers',
        on_delete=models.DO_NOTHING
    )
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
        