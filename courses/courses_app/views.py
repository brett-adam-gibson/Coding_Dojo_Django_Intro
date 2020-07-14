from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Course, Description, Comment
# Create your views here.

def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    errors = Course.objects.validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)

    else:
        course = Course.objects.create(name=request.POST['name'])
        desc = Description.objects.create(description=request.POST['description'])
        course.description = desc
        course.save()

    return redirect('/')

def create_comments(request, course_id):
    errors = Comment.objects.validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
    else:
        Comment.objects.create(
            comment=request.POST['comment'],
            course=Course.objects.get(id=course_id)
        )
    return redirect(f'/{course_id}')

def delete(request, course_id):
    if request.method == 'GET':
        context = {
            'course': Course.objects.get(id=course_id)
        }
        return render(request, 'delete.html', context)

    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        course.delete()
        return redirect('/')

def comments(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'comments.html', context)
