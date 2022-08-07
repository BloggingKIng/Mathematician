from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from . import views

app_name = 'quiz'

urlpatterns =[
    path('', TemplateView.as_view(template_name='Quiz\index.html')),
    path('quiz/solver/<int:id>/', view=views.submit, name='solver'),
    path('<str:test>/', view=views.quiz),
    path('test/submission/<int:test_id>/<int:submission_id>/result/',views.show_exam_result, name='show_exam_result'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)