from django.contrib import admin
from django.urls import path
from djangoapp import views

urlpatterns = [
    path('',views.navbar,name="navbar"),
    path('post',views.post,name='post'),
    path('post/<int:pk>',views.detail,name="detail"),
    path('gall/', views.gallery,name="gallery"),
    path('conta/', views.contact,name="contact"),
   
]