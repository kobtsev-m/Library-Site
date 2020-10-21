from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse
from django.template import loader
from library.models import Book, ContentImage, Comment
from django.utils import timezone

def main_page(request):
    template = loader.get_template("main_page.html")

    preview_images = ContentImage.objects.filter(name__startswith="preview")
    preview_images = {obj.name: obj.image for obj in preview_images}

    main_data = {
        "title": "Book shop",
        "images": preview_images
    }

    return HttpResponse(template.render(main_data, request))


def books(request):
    template = loader.get_template("books/content/books_table.html")

    books = Book.objects.all()
    header_img = ContentImage.objects.filter(name="header_books").first()
    header_img = header_img.image

    books_data = {
        "title": "Books",
        "header_img": header_img,
        "books": books,
        "last_page": "base"
    }

    return HttpResponse(template.render(books_data, request))


def book_page(request, isbn):
    template = loader.get_template("books/content/book_page.html")

    book = Book.objects.filter(ISBN=isbn)
    if book.exists():
        book = book.first()
    else:
        raise Http404("Страница не найдена")

    comments = book.comment_set.order_by('-date')

    book_data = {
        "title": book.title,
        "book": book,
        "comments": comments,
        "last_page": "library:base"
    }

    return HttpResponse(template.render(book_data, request))


def add_comment(request, isbn):
    if request.method == "POST":
        name = request.POST['name']
        comment = request.POST['comment']

        if not name or not comment:
            return redirect(reverse('library:book_page', args=(isbn,)))
        else:
            book = Book.objects.filter(ISBN=isbn).first()
            Comment.objects.create(
                name=name,
                comment=comment,
                book=book,
                date=timezone.now()
            )

    return redirect(reverse('library:book_page', args=(isbn,)))


def add_vote(request, vote):
    if request.method == "POST":
        book_id = request.POST['id']
        if not book_id:
            return redirect(reverse('library:base'))
        else:
            book = Book.objects.filter(id=book_id).first()

            if vote == "+":
                book.good_votes += 1
            else:
                book.bad_votes += 1

            book.save()

    return redirect(reverse('library:base'))
