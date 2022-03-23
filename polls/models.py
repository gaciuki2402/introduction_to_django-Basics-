from email.policy import default
from django.db import models

class Questions(models.Model):
    question_text =models.CharField(max_length=200)
    pub_date=models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Musician(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

class Album(models.Model):
    artist=models.ForeignKey(Musician, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField()
    num_stars=models.IntegerField()



# Create your models here.
