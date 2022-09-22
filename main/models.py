from django.db import models

# Create your models here.
class Task(models.Model):
    fullnames=models.CharField(max_length=100,blank=False)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.fullnames
