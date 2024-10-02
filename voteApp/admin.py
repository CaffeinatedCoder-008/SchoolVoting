from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "STUDENT COUNCIL ELECTIONS"
admin.site.site_title = "Voting Admin Area"
admin.site.index_title = "lorem ipsum dolor"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}), ('Date Tranformation',{'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)