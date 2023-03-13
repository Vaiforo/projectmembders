from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [
    {'title': "Home page", 'url_name': 'home'},
    {'title': "About us", 'url_name': 'about'},
    {'title': "Add page", 'url_name': 'add_page'},
    {'title': 'contact', 'url_name': 'contact'},
    {'title': "login", 'url_name': 'login'}
]


def index(request):
    posts = Members.objects.all()
    cats = Category.objects.all()
    context = {
        'title': 'Home page',
        'posts': posts,
        'menu': menu,
        'cats': cats,
    }
    return render(request, 'project_members/index.html', context=context)


def about(request):
    context = {
        'title': 'Home page',
        'menu': menu,
    }
    return render(request, 'project_members/about.html', context=context)


def addpage(request):
    return render(request, 'project_members/addpage.html', {'title': 'Add page', 'menu': menu})


def contact(request):
    # return render(request, 'project_members/contact.html', {'title': 'Contact page', 'menu': menu})
    return HttpResponse('contact page')


def login(request):
    # return render(request, 'project_members/login.html', {'title': 'Login page','menu': menu})
    return HttpResponse('login')


def post(request, post_id):
    post = Members.objects.get(id=int(post_id))
    context = {
        'title': 'Post',
        'menu': menu,
        'post': post,
    }
    return render(request, 'project_members/post.html', context=context)


def show_category(request, cat_id):
    posts = Members.objects.filter(cat_id=int(cat_id))
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
    context = {
        'title': 'Category',
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'cat_selected': cat_id,
    }
    return render(request, 'project_members/category.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
