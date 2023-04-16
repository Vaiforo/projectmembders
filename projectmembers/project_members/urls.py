from django.urls import path, re_path
from unicodedata import category

from .views import *

urlpatterns = [
    path('', ProjectsPage.as_view(), name='projects'),
    # path('hackathons/', hackathons, name='hackathons'),
    path('createpcard/', CreatePCard.as_view(), name='createpcard'),
    path('pcard/<int:pcard_id>/', PCard.as_view(), name='pcard'),
    path('pcardedit/<int:pcard_id>', PCardEdit.as_view(), name='pcardedit'),
    # path('createhcard/', createhcard, name='createhcard'),
    path('registration/', Registration.as_view(), name='registration'),
    path('profile/<int:profile_id>', Profile.as_view(), name='profile'),
    path('profiledit/<int:profile_id>', ProfileEdit.as_view(), name='profiledit'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
