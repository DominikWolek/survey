from django.contrib import admin
from api.models import Survey, Question, Answer, Lecture, Day, Place


class AnswerInLine(admin.TabularInline):
    model = Answer
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['value', 'single_select', 'survey']})
    ]
    inlines = [AnswerInLine]


class QuestioninLine(admin.TabularInline):
    model = Question
    extra = 0


class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name']})
    ]
    inlines = [QuestioninLine]

class PlaceInLine(admin.TabularInline):
    model = Place
    extra = 2

class DayAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['day']})
    ]
    inlines = [PlaceInLine]

class LectureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name', 'room', 'speaker', 'start_time', 'end_time']})
    ]
    list_display = ('name', 'speaker', 'attendance', 'average_rate')
    list_filter = ['start_time']

admin.site.register(Day, DayAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Lecture, LectureAdmin)
