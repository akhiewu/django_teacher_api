from django.db import models

# Create your models here.


class Teacher(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    designation = models.TextField(max_length=500)
    join_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
class Student(models.Model):
    Department = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Roll = models.IntegerField()
    Semester = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department    
    
    