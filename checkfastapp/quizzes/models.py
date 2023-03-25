from django.db import models
from accounts.models import Account


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    number_of_questions = models.IntegerField(default=0)
    is_public = models.BooleanField(default=False)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    content = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.content}, answer: {self.content}, correct: {self.correct}"


class QuizByAcc(models.Model):
    score = models.FloatField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.quiz)
