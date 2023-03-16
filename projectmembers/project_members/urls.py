from django.urls import path, re_path
from unicodedata import category

from .views import *

urlpatterns = [
    path('', projects, name='projects'),
    # path('hackathons/', hackathons, name='hackathons'),
    path('createpcard/', createpcard, name='createpcard'),
    path('pcard/<int:pcard_id>', pcard, name='pcard'),
    # path('createhcard/', createhcard, name='createhcard'),
    # path('registration/', registration, name='registration'),
    # path('authorization/', authorization, name='authorization'),
]
