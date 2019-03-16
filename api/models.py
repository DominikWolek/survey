import datetime

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Survey(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    def questions(self):
        return self.question_set


class Question(models.Model):
    value = models.CharField(max_length=200)
    answer_type = models.CharField(max_length=20, default='single-select')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
    def answers(self):
        return self.answer_set


class Answer(models.Model):
    value = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.content

class Day(models.Model):
    day = models.DateField('Day', default = timezone.localdate)

    def __str__(self):
        return str(self.day)

    def rooms(self):
        return self.place_set

class Place(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    room = models.CharField(max_length=100)

    def __str__(self):
        return str(self.room) + ' ' + str(self.day)

    def lectures(self):
        return self.lecture_set

    # @property
    # def id(self):
    #     if self.room == 'SFI Enterprise 1.38':
    #         return 1
    #     else:
    #         return 2

class Lecture(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.TimeField('Start time of lecture', default=timezone.localtime)
    end_time = models.TimeField('End time of lecture', default=(timezone.localtime))
    room = models.ForeignKey(Place, on_delete=models.CASCADE)
    speaker = models.CharField(max_length=200)
    rates = ArrayField(base_field=models.SmallIntegerField(blank=False), size=5, default=list([0 for x in range(5)]))

    def __str__(self):
        return self.name
    
    def attendance(self):
        return sum(self.rates)

    def average_rate(self):
        if self.attendance() == 0:
            return 0

        sum_of_rates = 0
        for i in range(len(self.rates)):
            sum_of_rates += (i + 1) * self.rates[i]

        return sum_of_rates / self.attendance()
