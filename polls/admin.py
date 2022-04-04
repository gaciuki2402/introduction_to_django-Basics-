<<<<<<< HEAD
from django.contrib import admin
<<<<<<< HEAD
from polls.models import Post

admin.site.register(Post)
 
=======
<<<<<<< HEAD
from .models import Question
admin.site.register(Question)
=======
>>>>>>> c979997c2e55e1eea0d57b172d424e32f685934d
>>>>>>> eadf4933b17b4f1e48aa6f604a342fb4573953d9
=======
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

>>>>>>> c5cfede35fded4403fe8b335a6b75cf8207eecfa

# Register your models here.
