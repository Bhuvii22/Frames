from django.contrib import admin
from django.urls import path,include
from framy import views

urlpatterns = [
   
    path('frame',views.frame),
    path('image',views.image)
]