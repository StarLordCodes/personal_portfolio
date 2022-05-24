from django.db import models


class Blog(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
