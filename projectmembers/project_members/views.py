import profile
import sys

from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages import success
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import *
from .models import *

# menu = [
#     {'title': "PM-Projects", 'url_name': 'projects'},
#     {'title': "PM-Hackathons", 'url_name': 'hackathons'},
#     {'title': "PM-CreatePCard", 'url_name': 'createpcard'},
#     {'title': "PM-CreateHCard", 'url_name': 'createhcard'},
#     {'title': "PM-Registration", 'url_name': 'registration'},
#     {'title': 'PM-Authorization', 'url_name': 'authorization'},
# ]

hrefs = {
    'toprojects': '/',
    'tocreatepcard': '/createpcard',
    'toregistration': '/registration',
    'tologin': '/login'
}


class ProjectsPage(ListView):
    model = Card
    template_name = 'project_members/projects.html'
    context_object_name = 'cards'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hrefs'] = hrefs
        context['title'] = 'PM-Projects'
        return context

    # def get_queryset(self):  # Filter
    #     return Card.objects.all()


class CreatePCard(CreateView):
    form_class = AddCardForm
    template_name = 'project_members/createpcard.html'
    success_url = reverse_lazy('projects')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PM-CreatePCard'
        context['hrefs'] = hrefs
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user if self.request.user.is_authenticated else None,
        })
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.had_tg_vk():
                if request.method.lower() in self.http_method_names:
                    handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
                else:
                    handler = self.http_method_not_allowed
                return handler(request, *args, **kwargs)
            else:
                return redirect(request.user.get_edit_absolute_url())
        else:
            return redirect('login')


class PCard(DetailView):
    model = Card
    template_name = 'project_members/pcard.html'
    # slug_url_kwarg = 'pcard_slug'
    pk_url_kwarg = 'pcard_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PM-PCard'
        context['hrefs'] = hrefs
        context['profile'] = PMUser.objects.get(pk=kwargs['object'].author.pk)
        return context


class PCardEdit(UpdateView):
    model = Card
    form_class = EditCardForm
    template_name = 'project_members/pcardedit.html'
    pk_url_kwarg = 'pcard_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PM-PCardEdit'
        context['hrefs'] = hrefs
        return context


class Profile(DetailView):
    model = PMUser
    template_name = 'project_members/profile.html'
    pk_url_kwarg = 'profile_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PM-Profile'
        context['hrefs'] = hrefs
        context['profile'] = PMUser.objects.get(pk=kwargs['object'].pk)
        return context


class ProfileEdit(UpdateView):
    model = PMUser
    form_class = EditUserForm
    template_name = 'project_members/profiledit.html'
    pk_url_kwarg = 'profile_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PM-ProfileEdit'
        context['hrefs'] = hrefs
        return context


class Registration(CreateView):
    form_class = RegisterUserForm
    template_name = 'project_members/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PM-Registration'
        context['hrefs'] = hrefs
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('projects')


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'project_members/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PM-Login'
        context['hrefs'] = hrefs
        return context

    def get_success_url(self):
        return reverse_lazy('projects')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
