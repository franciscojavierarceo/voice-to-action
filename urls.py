# urls.py
from django.urls import path
from .views import recording

urlpatterns = [
    path('recording/', recording, name='recording'),
]
