from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
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


@login_required
def about(request):
    return render(request, 'researchers/about.html', {'menu': menu, 'title': 'О нас'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'researchers/addpage.html'
    success_url = reverse_lazy(
        'home'
    )  # using instead .models.Researchers.get_absolute_url, reverse
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


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


""" def login(request):
    return HttpResponse("Авторизация") """


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


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'researchers/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'researchers/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')
