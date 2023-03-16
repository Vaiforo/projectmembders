from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [
    {'title': "PM-Projects", 'url_name': 'projects'},
    # {'title': "PM-Hackathons", 'url_name': 'hackathons'},
    {'title': "PM-CreatePCard", 'url_name': 'createpcard'},
    # {'title': "PM-CreateHCard", 'url_name': 'createhcard'},
    # {'title': "PM-Registration", 'url_name': 'registration'},
    # {'title': 'PM-Authorization', 'url_name': 'authorization'},
]


def projects(request):
    cards = Card.objects.all()
    context = {
        'menu': menu,
        'cards': cards,
    }
    return render(request, 'project_members/projects.html', context=context)


# def hackathons(request):
#     context = {
#         'menu': menu,
#     }
#     return render(request, 'project_members/hackathons.html', context=context)


def createpcard(request):
    if request.method == 'POST':
        form = AddCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddCardForm()
    context = {
        'menu': menu,
        'form': form,
    }
    return render(request, 'project_members/createpcard.html', context=context)


def pcard(request, pcard_id):
    card = get_object_or_404(Card, pk=pcard_id)
    context = {
        'card': card,
        'menu': menu,
    }
    return render(request, 'project_members/pcard.html', context=context)


# def createhcard(request):
# if request.method == 'POST':
#     form = AddPostForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
# else:
#     form = AddPostForm()
# context = {
#     'menu': menu,
#     'form': form,
# }
# return render(request, 'project_members/createhcard.html', context=context)


# def registration(request):
# if request.method == 'POST':
#     form = AddPostForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
# else:
#     form = AddPostForm()
# context = {
#     'menu': menu,
#     'form': form,
# }
# return render(request, 'project_members/registration.html', context=context)


# def authorization(request):
# if request.method == 'POST':
#     form = AddPostForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
# else:
#     form = AddPostForm()
# context = {
#     'menu': menu,
# 'form': form,
# }
# return render(request, 'project_members/authorization.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
