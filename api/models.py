import datetime

from django.db import models
from django.contrib.postgres.fields import ArrayField

class Survey(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    content = models.CharField(max_length=200)
    surveys = models.ManyToManyField(Survey)
    answer_type = models.CharField(max_length=20, default='single-select')

    def __str__(self):
        return self.content

class Answer(models.Model):
    content = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.content
    
class Lecture(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField
    duration = models.DurationField(default=datetime.timedelta(minutes=75))
    room = models.CharField(max_length=200)
    rates = ArrayField(base_field=models.SmallIntegerField(blank=False), size=5, default=list([0 for x in range(5)]))

    def __str__(self):
        return self.name
    
    def attendance(self):
        return sum(self.rates)

    def average_rate(self):
        if self.attendance() == 0:
            return 0

        sumOfRates = 0
        for i in range(len(self.rates)):
            sumOfRates += (i + 1) * self.rates[i]

        return (sumOfRates / self.attendance())