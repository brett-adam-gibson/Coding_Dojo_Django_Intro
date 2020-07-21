from django.shortcuts import render, redirect
from django.contrib import messages
from users_app.models import User
from .models import Post, Comment



# Create your views here.
def the_wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'posts': Post.objects.all(),
        'comments': Comment.objects.all(),
    }
    return render(request, 'the_wall.html', context)

def create_posts(request):
    #are there errors?
    errors = Post.objects.validate(request.POST)

    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/posts')

    logged_user = User.objects.get(id=request.session['user_id'])
    Post.objects.create(
        title=request.POST['title'],
        content=request.POST['content'],
        author=logged_user
    )
    return redirect('/posts')

def delete_post(request, post_id):
    #logged_user = User.objects.get(id=request.session['user_id'])
    to_delete = Post.objects.get(id=post_id)

    if to_delete.author_id == request.session['user_id']:
        to_delete.delete()
    return redirect('/posts')

def add_comment(request, post_id):
    #are there errors?
    errors = Comment.objects.validate(request.POST)

    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/posts')

    logged_user = User.objects.get(id=request.session['user_id'])
    this_post = Post.objects.get(id=post_id)
    print('i got this far')
    Comment.objects.create(
        comment_content=request.POST['comment_content'],
        comment_author=logged_user,
        post_message=this_post,
    )
    return redirect('/posts')
