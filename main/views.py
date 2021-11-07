from django.shortcuts import render

from main.models import *


def index(request):
    genres = Genre.objects.all()

    return render(request, 'main/index.html', {"genres": genres})


def book_list(request, slug):
    books = Book.objects.filter(genre__slug=slug)
    return render(request,
                  'main/book_list.html',
                  {'books': books}
                  )


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    authors_books = author.books.all()
    return render(request, 'main/author_detail.html', {'author': author, 'author_books': authors_books})

