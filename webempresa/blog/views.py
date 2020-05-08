from django.shortcuts import render
from .models import Entradas

# Create your views here.

def blog(request):
    entradass = Entradas.objects.all()
    return render(request, "blog/blog.html", {'entradass':entradass})