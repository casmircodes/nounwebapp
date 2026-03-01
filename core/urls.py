from django.urls import path
from . import views


urlpatterns = [
    path('',  views.index, name="index"),
    path('past-questions/',  views.past_questions, name="past_questions")
]