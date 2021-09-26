from django.db import models

# Create your models here.
from django.db import models

class student(models.Model):            #Table Definition
    name=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.name
