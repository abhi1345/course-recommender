from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Row(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=10)
