from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.last_name} {self.user_name}'

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    student_id = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.last_name} {self.user_name}'

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    teachers = models.ManyToManyField(Teacher)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.name} {self.description}'

class Subject(models.Model):
    name = models.CharField(max_length=50)


# Create your models here.
