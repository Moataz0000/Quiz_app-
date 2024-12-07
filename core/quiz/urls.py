from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'quiz'




router = DefaultRouter()
router.register(r'questions', views.QuestionListView, basename='questions')

urlpatterns = router.urls + [
    path('check-answer/', views.CheckAnswerView.as_view(), name='check-answer'),
]
