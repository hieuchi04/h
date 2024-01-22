from django.contrib import admin
from django import forms
from apps.exams.models import Exams,Result
from apps.subjects.models import Questions, Subjects


class QuestionsInline(admin.StackedInline):
    model = Questions
    extra = 0


class ExamsAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]
    list_display = ["id", "exam_name", "user_id", "time_limit", "active"]
    list_editable = ('active',)
    

class ResultAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "exam_id", "time_finish", "score", "active"]
    list_editable = ('active',)


admin.site.register(Exams, ExamsAdmin,)
admin.site.register(Result, ResultAdmin)

