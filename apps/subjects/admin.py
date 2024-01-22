from django.contrib import admin
from .models import Subjects, Questions, Answers
# Register your models here.

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ["id", "subject_name", "active"]
    list_editable = ('active',)


class AnswersAdmin(admin.StackedInline):
    model = Answers
    extra = 0


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["id", "subject_id", "question_text", "active"]
    list_editable = ('active',)
    inlines = [AnswersAdmin]


admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Questions, QuestionsAdmin)