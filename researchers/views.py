from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Researchers.objects.all()
    return render(
        request,
        'researchers/index.html',
        {'posts': posts, 'menu': menu, 'title': 'Главная страница'},
    )


def about(request):
    return render(request, 'researchers/about.html', {'menu': menu, 'title': 'О нас'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
