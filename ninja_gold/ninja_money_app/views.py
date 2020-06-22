
# from django.shortcuts import render, redirect
# def index(request):
#     if 'gold' in request.session:
#         return render(request, 'index.html')
#     else:
#         request.session['gold'] = 0
#         return render(request, 'index.html')

# def process_money(request):
#     print(request.POST['place'])

#     return redirect('/')


# def reset(request):
#     if request.method == 'POST':
#         request.session['gold'] = 0
#         request.session['activities'] = []
#     return redirect('/')


from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'total_gold' not in request.session or 'activities' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            gold = random.randint(10, 21)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['building'] == 'cave':
            gold = random.randint(5, 11)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['building'] == 'house':
            gold = random.randint(2,6)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['building'] == 'casino':
            gold = random.randint(-50, 51)
            if gold >= 0:
                request.session['activities'].append('Entered a casino and earned ' + str(gold) +' gold' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            else:
                request.session['activities'].append('Entered a casino and lost ' + str(gold) + ' gold... Ouch...' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        request.session['total_gold'] += gold

    return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return redirect('/')