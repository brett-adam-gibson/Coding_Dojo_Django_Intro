from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

# Create your views here.
def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    errors = Show.objects.form_validation(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/shows/new')
    # if len(errors) > 0:
    #     for key, vlaue in errors.items():
    #         messages.error(request, value)
    #     return redirect('/')
    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description'])
    return redirect('/')

def show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'show.html', context)

def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }

    return render(request, 'edit.html', context)

def delete(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')

def update(request, show_id):
    errors = Show.objects.form_validation(request.POST)
    to_update = Show.objects.get(id=show_id)

    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
        # return redirect('/shows/' + show_id + '/edit')

    to_update.title = request.POST['title']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    to_update.save()
    return redirect('/shows')
