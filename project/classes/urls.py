from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='class_list'),
]