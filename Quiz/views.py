from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.
def quiz(request,test):
    test = Test.objects.get(name=test)
    # for tests in test.question_set.all():
    #     print(tests.question_text)
    return render(request,'Quiz/assignment.html', {'test':test})


def extract_answers(request):
   submitted_anwsers = []
   for key in request.POST:
       if key.startswith('choice'):
           value = request.POST[key]
           choice_id = int(value)
           submitted_anwsers.append(choice_id)
   return submitted_anwsers


def submitted(request, answers):
    return HttpResponse(answers)

def submit(request, id):
    test = get_object_or_404(Test, pk=id)

    choices = extract_answers(request)
    submission = Submission.objects.create()
    for choice in choices:
        print(choice)
        submission.choices.add(choice)
    return HttpResponseRedirect(reverse(viewname='quiz:show_exam_result', args=(test.id,submission.id)))


def show_exam_result(request, test_id, submission_id):
    test = get_object_or_404(Test, pk=test_id)
    choices =  Submission.objects.get(id=submission_id)
    total_marks = 0
    marks = 0
    context = {}
    qs = [ids.choice_qs.id for ids in choices.choices.all()]

    
    dup = []
    for id in qs:
        if id not in dup:
            dup.append(id)
    corrQs = []
    for querries in dup:
        for i in Question.objects.get(id=querries).answer_set.all():
            if i.is_correct:
                print(i.choice_text)
                total_marks += i.choice_qs.question_mark
                
            
            if i.is_correct and i not in choices.choices.all():
                pass
            elif i.is_correct and i in choices.choices.all():
                print(i.choice_text)
                marks += i.choice_qs.question_mark
                print('WOW')
                corrQs.append(i.choice_qs)
                print(marks)
            elif not i.is_correct and i in choices.choices.all():
                if i.choice_qs in corrQs:
                    marks -= i.choice_qs.question_mark

                    corrQs.remove(i.choice_qs)

    if marks < 0:
        marks = 0
    grade = (marks/total_marks) * 100
    grade = '{}'.format(grade)
    context['grade'] = float(grade)
    context['total'] = int(total_marks)
    context['marks'] = int(marks)
    context['Question'] = qs
    context['course'] = test
    context['selected'] = choices.choices.all()

    return render(request, 'quiz/result.html', context)