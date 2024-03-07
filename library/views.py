from django.shortcuts import render
from .models import Book, Student, Bookings

def landingView(request):
    return render(request, 'library/landing.html')

def books_view(request):
    books = Book.objects.all()
    return render(request, 'library/books.html', {''})



# Create your views here.
