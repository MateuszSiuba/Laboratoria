from django.urls import path
from . import views

urlpatterns = [
    path('', views.licznik_odwiedzin, name='licznik'),
]