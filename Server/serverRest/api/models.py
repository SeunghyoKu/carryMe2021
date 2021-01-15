from django.db import models

# Create your models here.
class Example(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=40)
    numView = models.IntegerField()

