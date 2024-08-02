from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/',views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('third/', views.third_view, name='third_view'), 
    path('second/', views.second_view, name='second_view'), 
    path('registers/', views.registers, name='registers'),
    
]