from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
