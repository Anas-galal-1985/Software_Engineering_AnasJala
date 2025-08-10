from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('show/', views.showw, name='show'),
    path('edit/', views.editt, name='edit'),
    path('delete/', views.dell, name='delete'),
]
