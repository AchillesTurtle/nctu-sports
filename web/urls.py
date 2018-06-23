from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('anncs/<int:pk>', views.anncdetail, name='anncdetail'),
    path('anncs/add', views.anncadd, name='anncadd'),
    path('anncs/edit/<int:pk>', views.anncedit, name='anncedit'),
    path('anncs/delete/<int:pk>', views.anncdelete, name='anncdelete'),
]
