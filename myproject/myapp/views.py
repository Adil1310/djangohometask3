from django.shortcuts import render

# Create your views here.

def loginmenu(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'homepage.html')

def registration(request):
    return render(request, 'registration.html')

def newsitem(request):
    return render(request, 'newsitem.html')