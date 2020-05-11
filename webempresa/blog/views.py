from django.shortcuts import render, get_object_or_404
from .models import Entradas, Category

# Create your views here.

def blog(request):
    entradass = Entradas.objects.all()
    return render(request, "blog/blog.html", {'entradass':entradass})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})