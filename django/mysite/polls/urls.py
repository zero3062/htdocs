from django.urls import path

from . import views

urlpatterns = [
    path('', ciews.index, name='index'),
]
