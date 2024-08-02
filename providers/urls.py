from django.urls import path
from . import views

app_name = 'providers'

urlpatterns = [
    path('',views.ServiceListView.as_view(), name='service_list'),
    path('<slug:slug>/', views.CategoryListView.as_view(), name='category_list'),
    path('<str:service>/<slug:slug>/', views.DescriptionListView.as_view(), name='descript_list'),
    path('third/', views.third_view, name='third_view'),
    path('registers/', views.registers, name='registers'),




   

]

