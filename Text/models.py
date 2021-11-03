from django.db import models

# Create your models here.

class Text(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField('date published')
    user=models.CharField(max_length=200)


class Tag(models.Model):
    title = models.ForeignKey('Text',
    on_delete=models.CASCADE,)
    