from django.shortcuts import render, redirect
from django.contrib import messages
from login_reg_app.models import User
from .models import Book


# Create your views here.
def fav_books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_books': Book.objects.all()
    }
    print(request.session['user_id'])
    return render(request, 'fav_books.html', context)

def add_fav_book(request):
    errors = Book.objects.book_validator(request.POST)

    if errors:
        for value in errors.values():
            messages.error(request, value, extra_tags='add_book')
        return redirect('/fav_books')
    else:
        user = User.objects.get(id=request.session['user_id'])
        book = Book.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            uploaded_by=user,
        )
        user.liked_books.add(book)

        return redirect(f'/fav_books/{book.id}')

def view_book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "one_book.html", context)


def update(request, book_id):
    book = Book.objects.get(id=book_id)
    book.description = request.POST['description']
    book.save()

    return redirect(f"/fav_books/{book_id}")

def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()

    return redirect('/fav_books')

def favorite(request, book_id):
    user = User.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=book_id)
    user.liked_books.add(book)

    return redirect('/fav_books')

def unfavorite(request, book_id):
    user = User.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=book_id)
    user.liked_books.remove(book)

    return redirect('/fav_books')

def logout(request):
    request.session.flush()

    return redirect('/')
