from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField(default=0)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id} {self.title} {self.description}"

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    birth_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.name} {self.last_name}"

class Bookings(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    returned_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.id} {self.student.name} {self.book}"
