# request handler for action
# request -> response

from django.shortcuts import render
from django.http import HttpResponse

# def say_hello(request):
#     return HttpResponse('Hello World')

# call the html and print with urls.py

def calculate():
    x = 1
    y = 2
    return x
    
def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Mosh'})
 