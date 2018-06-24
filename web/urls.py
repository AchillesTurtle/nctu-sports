from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('anncs/<int:pk>/', views.anncdetail, name='anncdetail'),
    path('anncs/add/', views.anncadd, name='anncadd'),
    path('anncs/edit/<int:pk>/', views.anncedit, name='anncedit'),
    path('anncs/delete/<int:pk>/', views.anncdelete, name='anncdelete'),

    path('events/', views.eventlist, name='eventlist'),
    path('events/status/<int:pk>/', views.eventstatus, name='eventstatus'),
    path('events/add', views.eventadd, name='eventadd'),
    path('events/edit/<int:pk>', views.eventedit, name='eventedit'),
    path('events/delete/<int:pk>', views.eventdelete, name='eventdelete'),
    path('events/signup/<int:pk>', views.eventsignup, name='eventsignup'),
]
