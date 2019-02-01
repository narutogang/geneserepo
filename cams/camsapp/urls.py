from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from camsapp import views

#for template tagging
app_name='camsapp'

urlpatterns = [
path('relative/',views.relative,name='relative'),

path('user_login/', views.user_login, name='user_login'),

path('other/',views.other,name='other'),
path('register/',views.register,name='register'),

path('index/', views.index, name='index'),
path('users/', views.users, name='users'),
path('formpage/', views.form_name_view, name='form_name'),
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),


]
