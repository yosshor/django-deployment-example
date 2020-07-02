from django.contrib import admin
from django.urls import path,include
from five_app import views

app_name = 'five_app'

urlpatterns = [
    path('',views.base,name='base'),
    path('index',views.index, name='index'),
    path('help',views.help, name='help'),
    path('form',views.form, name='form'),
    # path('media',views.media, name='media'),
    path('logout',views.user_logout,name='user_logout'),
    path('login',views.user_login,name='login'),
    path('special',views.special,name='special'),

    path('register',views.register,name='register'),
    path('admin/', admin.site.urls),
]