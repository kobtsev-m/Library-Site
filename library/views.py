from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse
from django.template import loader
from library.models import PublishingHouse, Book, ContentImage, Comment
from django.utils import timezone
from pycountry import countries

def main_page(request):
    template = loader.get_template("index.html")

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
        "last_page": reverse('base')
    }

    return HttpResponse(template.render(books_data, request))


def book_page(request, isbn):
    template = loader.get_template("books/content/book_page.html")

    book = Book.objects.filter(ISBN=isbn)
    if book.exists():
        book = book.first()
        book.author.country = countries.get(alpha_2=book.author.country).name
    else:
        raise Http404("Страница не найдена")

    comments = book.comment_set.order_by('-date')
    last_page = request.META.get('HTTP_REFERER', reverse('base'))

    book_data = {
        "title": book.title,
        "book": book,
        "comments": comments,
        "last_page": last_page
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
            return redirect(reverse('library:books'))
        else:
            book = Book.objects.filter(id=book_id).first()

            if vote == "+":
                book.good_votes += 1
            else:
                book.bad_votes += 1

            book.save()

    return redirect(reverse('library:books'))

def ph(request):
    template = loader.get_template("ph/ph_table.html")

    ph = PublishingHouse.objects.all()
    for cur_ph in ph:
        cur_ph.country = countries.get(alpha_2=cur_ph.country).name
        cur_ph.books = cur_ph.book_set.all()

    ph_data = {
        "title": "Publishing houses",
        "ph": ph,
        "last_page": reverse('base')
    }

    return HttpResponse(template.render(ph_data, request))