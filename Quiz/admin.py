from django.contrib import admin
from .models import Test, Answer, Submission, Question

# Register your models here.

class AnswerInline(admin.StackedInline):
    model= Answer
    extra = 0

class QuestionInline(admin.StackedInline):
    model= Question
    extra = 15


class QuestionAdmin(admin.ModelAdmin):
    inlines= [AnswerInline]
    list_display = ['question_text']

class TestAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Test,TestAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)