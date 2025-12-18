from django.urls import path
from . import views

urlpatterns = [
    # Endpoint API (zwraca JSON)
    path('api/greet/', views.greet, name='greet_api'),
    # Strona dla użytkownika (zwraca HTML)
    path('', views.index, name='greet_view'),
]