from django.db import models


# Create your models here.
class Book(models.Model):
    ISBN = models.CharField(max_length=45, unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    translator = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
