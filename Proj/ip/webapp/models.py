import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models import (
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    OneToOneField,
    ForeignKey,
    )
# Create your models here.

class Idea(models.Model):
    user = ForeignKey(User, max_length=5, on_delete='CASCADE')
    text = CharField(max_length = 100, default = "No text")
    subject = CharField(max_length = 30, default ="No Subject")
    date_time =  DateTimeField('Date published',auto_now=True)


    def __str__(self):
        return self.subject

    def was_published_recently(self):
        return self.date_time >= timezone.now()-datetime.delta(days=1)

class Comments(models.Model):
    ctext = CharField(max_length = 50)
    user = ForeignKey(User, max_length = 5, on_delete = 'CASCADE')
    ideas = ForeignKey(Idea, max_length = 5, on_delete = 'CASCADE')
    date_time =  DateTimeField('Date published',auto_now=True)


    def was_published_recently(self):
        return self.date_time >= timezone.now()-datetime.delta(days=1)

class Like(models.Model):
    user = ForeignKey(User, max_length = 5, on_delete = 'CASCADE')
    ideas = ForeignKey(Idea, max_length = 5, on_delete = 'CASCADE')

