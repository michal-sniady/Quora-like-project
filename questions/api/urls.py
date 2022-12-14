from django.urls import include, path
from rest_framework.routers import DefaultRouter
from questions.api import views as qv

router = DefaultRouter()
router.register(r'questions', qv.QuestionViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<slug:slug>/answer/', qv.AnswerCreateAPIView.as_view(), name='answer-create')
]
