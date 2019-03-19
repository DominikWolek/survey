from rest_framework import serializers
from django.db.models import F
from .models import Survey, Question, Answer, Lecture, Place, Day


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'value')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'value', 'answers', 'answer_type')


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = ('id', 'name', 'questions')


class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'name', 'start_time', 'end_time', 'speaker')

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    lectures = LectureSerializer(many=True)
    id = serializers.SerializerMethodField('ide')

    class Meta:
        model = Place
        fields = ('id', 'room', 'lectures')

    def ide(self, obj):
        if obj.room == 'SFI Enterprise 1.38':
            return 1
        else:
            return 2


class DaySerializer(serializers.ModelSerializer):
    rooms = PlaceSerializer(many=True)

    class Meta:
        model = Day
        fields = ('day', 'rooms')        


class ManyResponsesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    answers = serializers.JSONField()


class ResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    closed = serializers.ListField(child=serializers.IntegerField(min_value = 0), required=False)
    open = serializers.CharField(required=False)


class RateSerializer(serializers.Serializer):
    rate = serializers.IntegerField()        


class RateSpecifiedSerializer(serializers.Serializer):
    lecture_id = serializers.IntegerField()
    rate = serializers.IntegerField()