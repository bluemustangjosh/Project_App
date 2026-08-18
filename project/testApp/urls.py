from django.urls import path
from .views import home, add_class_view

urlpatterns = [
    path('', home, name='home'),
    path('add_class/', add_class_view, name='add_class'),
    path('', include('testApp.urls')),
]
