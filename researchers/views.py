from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import *
from .models import *
from .utils import *


class ResearchersHome(DataMixin, ListView):
    model = Researchers
    template_name = 'researchers/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Researchers.objects.filter(is_published=True)


""" def index(request):
    posts = Researchers.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'researchers/index.html', context=context) """


def about(request):
    return render(request, 'researchers/about.html', {'menu': menu, 'title': 'О нас'})


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'researchers/addpage.html'
    # success_url = reverse_lazy('home') - using instead .models.Researchers.get_absolute_url, reverse

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return context


""" def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(
        request,
        'researchers/addpage.html',
        {'form': form, 'menu': menu, 'title': 'Добавление статьи'},
    ) """


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


""" def show_post(request, post_slug):
    post = get_object_or_404(Researchers, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'researchers/post.html', context=context) """


class ShowPost(DataMixin, DetailView):
    model = Researchers
    template_name = 'researchers/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class ResearchersCategory(DataMixin, ListView):
    model = Researchers
    template_name = 'researchers/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Researchers.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Категория - ' + str(context['posts'][0].cat),
            cat_selected=context['posts'][0].cat_id,
        )
        return dict(list(context.items()) + list(c_def.items()))


""" def show_category(request, cat_id):
    posts = Researchers.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'researchers/index.html', context=context) """
