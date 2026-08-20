#testApp urls.py
from django.urls import path
from .views import add_class_view 
urlpatterns = [
    path('add_class/', add_class_view, name='add_class'),
]
