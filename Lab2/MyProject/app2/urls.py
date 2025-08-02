from django.urls import path
from .views import Print_app2

urlpatterns = [
    path('', Print_app2),
]