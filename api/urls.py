from django.urls import path

from api import views

urlpatterns = [
    path('', views.api_home)  # localhost:8000/api/
]