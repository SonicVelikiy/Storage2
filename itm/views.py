from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Category,InProductList

def Home(request):
    if request.user.is_authenticated:
        data = Category.objects.all()
        return render(request, "home.html", {"category": data, "username": request.user})
    else:
        return render(request, "home.html")

def Storage(request):
    if request.user.is_authenticated:
        storage = InProductList.objects.all();
        category = Category.objects.all()
        return render(request, "storage.html", {"category": category, "storage":storage, "username": request.user})