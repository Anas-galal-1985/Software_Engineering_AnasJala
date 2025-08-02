from django.urls import path
from .views import Print_app1

urlpatterns = [
    path('', Print_app1),
]