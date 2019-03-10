from django.contrib import admin
from api.models import Survey, Question, Answer, Lecture


class AnswerInLine(admin.TabularInline):
    model = Answer
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields' : ['content', 'single_select', 'survey']})
    ]
    inlines = [AnswerInLine]


class QuestioninLine(admin.TabularInline):
    model = Question
    extra = 0


class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields' : ['name']})
    ]
    inlines = [QuestioninLine]

class LectureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields' : ['name', 'room', 'speaker', 'start_time', 'duration']})
    ]
    list_display = ('name', 'speaker', 'attendance', 'average_rate')
    list_filter = ['start_time']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Lecture, LectureAdmin)