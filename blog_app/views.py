from typing import Any
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView


from .models import *
from .forms import *

# Create your views here.


class PostsView(ListView):
    model = Post
    template_name = 'blog_app/posts.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Посты'}


class AddPostView(CreateView):
    form_class = AddPostForm
    template_name = 'blog_app/add_post.html'
    success_url = reverse_lazy('home')
    raise_exception = True
    extra_context = {'title': 'Добавить Пост'}

    def get_initial(self):
        tmp = super().get_initial()
        tmp['user'] = self.request.user.pk
        return tmp


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog_app/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'blog_app/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self) -> str:
        return reverse_lazy('home')


def logout_user(request: HttpRequest):
    logout(request)
    return redirect('login')
