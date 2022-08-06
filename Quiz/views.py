from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def quiz(request,test):
    test = Test.objects.get(name=test)
    # for tests in test.question_set.all():
    #     print(tests.question_text)
    return render(request,'Quiz/assignment.html', {'test':test})
