from django.db import models
from accounts.models import Account
from django.db import models


class BlankTest(models.Model):
    title = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)

    date = models.DateField(auto_now=True, auto_now_add=True)
    question_count = models.IntegerField(default=10)
    question_mark = models.FloatField(default=1.0)
    num_of_choices = models.IntegerField(default=10)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TestByStudent(models.Model):

    student_id = models.IntegerField()
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    question_count = models.IntegerField(default=10)
    true_answers_count = models.IntegerField(default=0)
    question_mark = models.FloatField(default=1.0)
    score = models.FloatField()
    
    test = models.ForeignKey(BlankTest, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.quiz)
