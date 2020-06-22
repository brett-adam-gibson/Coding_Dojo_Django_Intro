from django.shortcuts import render
# from time import gmtime, strftime
import datetime

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    context = {
        # "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        "now": datetime.datetime.now()
    }
    return render(request, 'index.html', context)





