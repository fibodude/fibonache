from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.


def fiba(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a
		


def fibo(request):
    c = ''
    try:
        c = fiba(int(request.GET['fib']))
    except:
        c = 'Vvedi cheslo sverhu....))))))'
    context = {
        'fibo' : c,
    }
    return render_to_response('index.html', context)
	
