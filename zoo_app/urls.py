from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zoo', views.zoo, name='zoo'),
    path('recognizeImage', views.recognizeImage, name='recognizeImage'),
]
