from django.urls import path
from . import views

urlpatterns = [
     path('', views.homepage, name='homepage'),
    path('add_hospital/', views.add_hospital, name='add_hospital'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_inventory/', views.add_inventory, name='add_inventory'),
    path('view_inventory/', views.view_inventory, name='view_inventory'),
]
