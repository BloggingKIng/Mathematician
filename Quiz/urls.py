from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('', TemplateView.as_view(template_name='Quiz\index.html')),
    path('<str:test>/', view=views.quiz)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)