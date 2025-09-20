from django.db import models
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
# Create your models here.
