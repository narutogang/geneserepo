
from django.contrib import admin
from django.urls import path, include
from camsapp import views

urlpatterns = [
    path('',include('camsapp.urls',namespace='camsapp')),
    path('',views.index,name='index'),
    path('other/',views.other,name='other'),
    path('admin/', admin.site.urls),
    path('formpage/',views.form_name_view,name='form_name'),
    path('users/',views.users,name='users'),
    path('logout/', views.user_logout,name='logout'),
    path('speical/',views.special,name='special'),
]
