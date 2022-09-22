from django.urls import path
from . import views

# /agenda
urlpatterns = [
    path('', views.index)
]