from django.shortcuts import render

# Create your views here.


def home(request):
    name = 'Bob'
    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'Andrey'
    return render(request, 'about.html', {'name': name})