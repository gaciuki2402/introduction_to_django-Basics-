from secrets import choice
from django.contrib import admin

from .models import Questions,Choice,Musician,Album

admin.site.site_header="polls Admin"
admin.site.site_title="polls Admin Area"
admin.site.index_title="Welcome to polls Admin Area"
admin.site.register(Musician,Album)

class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldset=[(None, {'fields':['question_text']}),
    ('Date Information', {'fields':['pub_date'], 'classes': ['collapse']}),]
    inlines=[ChoiceInLine]

admin.site.register(Questions,QuestionAdmin)


# Register your models here.
