from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    rollNo = models.IntegerField()
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name
