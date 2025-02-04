from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения women")


def categories(request):
    return HttpResponse("<h1>Статьи по категория</h1>")


def about(request):
    return HttpResponse("О сайте")
