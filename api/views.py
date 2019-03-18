from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Survey, Question, Answer, Lecture, Day
from .serializers import SurveySerializer, QuestionSerializer, AnswerSerializer, LectureSerializer, DaySerializer, RateSerializer, ResponseSerializer, RateSpecifiedSerializer

class SurveyViewSet(viewsets.ModelViewSet):
    paginator = None
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    @action(detail=True, methods=['post'])
    def reply(self, request, pk=None):
        serializer = ResponseSerializer(data=request.data, many=True)
        
        if serializer.is_valid():
            for data in serializer.data:
                for id in data['closed']:
                    answer = Answer.objects.get(pk=id)
                    answer.votes += 1
                    answer.save()
            return Response({"status" : "survey_filled"})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            

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
        lecture = Lecture.objects.get(pk=pk)
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid() and 1 <= serializer.data['rate'] <= 5 :
            lecture.rate_lecture(serializer.data['rate'])
            lecture.save()
            return Response({'status' : 'lecture_rated'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def rates(self, request):
        serializer = RateSpecifiedSerializer(data=request.data, many=True)
        if serializer.is_valid():
            for data in serializer.data:
                if not(1 <= data['rate'] <= 5):
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                lecture = Lecture.objects.get(pk=data['lecture_id'])
                lecture.rate_lecture(data['rate'])
                lecture.save()
            return Response({'status' : 'lectures_rated'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)