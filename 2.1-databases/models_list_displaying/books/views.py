from django.shortcuts import render
from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def books_on_date_view(request, pub_date):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.filter(pub_date=pub_date),
        'prev_book': Book.objects.order_by('-pub_date').exclude(pub_date__gte=pub_date).first(),
        'next_book': Book.objects.order_by('pub_date').filter(pub_date__gt=pub_date).first(),
    }
    return render(request, template, context)

