from django.contrib import admin
from .models import Book, Bookings, Student

admin.site.register(Book)
admin.site.register(Bookings)
admin.site.register(Student)

# Register your models here.
