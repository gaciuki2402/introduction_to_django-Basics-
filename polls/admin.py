from secrets import choice
from django.contrib import admin

from .models import Questions,Choice,Musician,Album

admin.site.site_header="polls Admin"
admin.site.site_title="polls Admin Area"
admin.site.index_title="Welcome to polls Admin Area"

class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldset=[(None, {'fields':['question_text']}),
    ('Date Information', {'fields':['pub_date'], 'classes': ['collapse']}),]
    inlines=[ChoiceInLine]

admin.site.register(Questions,QuestionAdmin)
admin.site.register(Musician)
admin.site.register(Album)


# Register your models here.
