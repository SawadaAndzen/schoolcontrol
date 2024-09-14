from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    
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
    students_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    
class Schedule(models.Model):
    day = models.CharField(max_length=10, choices=[("Monday","Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"), ("Thursday", "Thursday"), ("Friday", "Friday")])
    begining = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    s_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    s_teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.day}: {self.begining}"
    
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    g_subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    grade = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student}: grade is {self.grade}"