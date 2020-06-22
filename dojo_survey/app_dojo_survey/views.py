from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'message': 'Welcome to this awesome website!'
    }
    return render(request, 'form.html', context)

def process(request):
    if request.method == 'POST':
        # print(request.POST['name'])
        # print(request.POST['language'])
        # print(request.POST['location'])
        request.session['name'] = request.POST['name']
        request.session['language'] = request.POST['language']
        request.session['location'] = request.POST['location']
    return redirect('/result')

def result(request):
    context = {
        'name': request.session['name'],
        'language': request.session['language'],
        'location': request.session['location']
    }
    return render(request, 'result.html', context)
