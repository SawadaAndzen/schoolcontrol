from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        
        return self.name
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subject = models.ManyToManyField(Subject)
    
    def __str__(self):
        
        return f"{self.name} {self.surname}"
    
    
class Class(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    
    def __str__(self):
        
        return f"{self.name}({self.grade})"
    
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    students_class = models.ManyToManyField(Class)
    
    def __str__(self):
        
        return f"{self.name} {self.surname}"