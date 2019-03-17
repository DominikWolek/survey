from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Survey, Question, Answer, Lecture, Day
from .serializers import SurveySerializer, QuestionSerializer, AnswerSerializer, LectureSerializer, DaySerializer, RateSerializer, ResponseSerializer

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

    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        lecture = self.get_object()
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid() and 1 <= serializer.data['rate'] <= 5 :
            lecture.rate_lecture(serializer.data['rate'])
            lecture.set()
            return Response({'status' : 'lecture rated'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
