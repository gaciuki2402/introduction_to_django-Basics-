<<<<<<< HEAD
from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
=======
from django.db import models

<<<<<<< HEAD
class Question(models.Model):
     question_text=models.CharField(max_length=200)
     pub_date=models.DateTimeField("date published")

class Choice(models.Model):
     question=models.ForeignKey(Question, on_delete=models.CASCADE)
     choice_text=models.CharField(max_length=200)
     votes=models.IntegerField("date published")

        



=======
>>>>>>> c979997c2e55e1eea0d57b172d424e32f685934d
# Create your models here.
>>>>>>> eadf4933b17b4f1e48aa6f604a342fb4573953d9
