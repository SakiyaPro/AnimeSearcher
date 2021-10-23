from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'search_anime'

urlpatterns = [
    path('genre_search/<genre>/',
        views.genre_search, name='genre_search'), 
]