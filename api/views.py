from django.shortcuts import render
from rest_framework import viewsets
from .models import Survey, Question, Answer, Lecture
from .serializers import SurveySerializer, QuestionSerializer, AnswerSerializer, LectureSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class LectureViewSet(viewsets.ModelViewSet):
    can_be_rated_ids = [lecture.id for lecture in Lecture.objects.all() if lecture.can_be_rated()] 
    queryset = Lecture.objects.filter(id__in=can_be_rated_ids).order_by('-start_time')        
    serializer_class = LectureSerializer
