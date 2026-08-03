from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('delete/<int:class_id>/', views.delete_class, name='delete_class'),
]