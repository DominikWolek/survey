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
    content = models.CharField(max_length=200)
    single_select = models.BooleanField(default=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
    def answers(self):
        return self.answer_set
    
    @property
    def answer_type(self):
        if self.single_select:
            return 'single-select'
        else:
            return 'open'


class Answer(models.Model):
    content = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.content
    
    
class Lecture(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField('Start time of lecture', default=timezone.now())
    duration = models.DurationField(default=datetime.timedelta(minutes=75))
    room = models.CharField(max_length=200)
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

    def can_be_rated(self):
        return (self.start_time + self.duration) >= (timezone.now() + datetime.timedelta(hours=1))
