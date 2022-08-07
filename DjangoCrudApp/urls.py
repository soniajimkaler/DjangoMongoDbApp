from django.contrib import admin
from django.urls import path,  include
from DjangoCrudApp import views


urlpatterns = [
    path('', views.add_post, name="add_post")
    
]
