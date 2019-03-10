from rest_framework import serializers
from .models import Survey, Question, Answer, Lecture


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'content')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'content', 'answer_type', 'answers')
        read_only_fields = ('answer_type',)


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Survey
        fields = ('id', 'name', 'questions')


class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = ('name', 'start_time', 'duration', 'room')