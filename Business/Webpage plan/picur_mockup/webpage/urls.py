from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kurzusok/', views.kurzusok, name='kurzusok'),
    path('kurzusok/kurzus1/', views.kurzus1, name='kurzus1'),
    path('kurzusok/kurzus2/', views.kurzus2, name='kurzus2'),
    path('kurzusok/kurzus3/', views.kurzus3, name='kurzus3'),
    path('kurzusok/kurzus4/', views.kurzus4, name='kurzus4'),
    path('iskolak/', views.iskolak, name='iskolak'),
]