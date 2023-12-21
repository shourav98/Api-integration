from django.db import models

# Create your models here.
class Ai(models.Model):
    tname = models.CharField(max_length=20)
    course_name = models.CharField(max_length=20)
    course_duration = models.IntegerField()
    seat = models.IntegerField()
