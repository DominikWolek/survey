from django.shortcuts import render
from rest_framework import viewsets
from .models import Survey, Question, Answer, Lecture, Day
from .serializers import SurveySerializer, QuestionSerializer, AnswerSerializer, LectureSerializer, DaySerializer

class SurveyViewSet(viewsets.ModelViewSet):
    paginator = None
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    paginator = None
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    paginator = None
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class LectureViewSet(viewsets.ModelViewSet):
    paginator = None
    queryset = Day.objects.all()
    serializer_class = DaySerializer
