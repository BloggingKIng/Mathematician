from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(default='', max_length=20)
    


class Question(models.Model):

    question_text = models.CharField(max_length=1000, default='What is the ans of 2 + 2')
    question_mark = models.IntegerField(default=2)
    Course = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)



class Answer(models.Model):
    choice_text = models.CharField(max_length=200)
    choice_qs = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct =  models.BooleanField(default=False)

class Submission(models.Model):
   choices = models.ManyToManyField(Answer)
   