from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('add-assignment/', views.add_assignment, name='add_assignment'),  
    path('api/assignments/<int:assignment_id>/toggle/', views.toggle_assignment_complete, name='toggle_assignment'),
    path('api/assignments/<int:assignment_id>/delete/', views.delete_assignment, name='delete_assignment'),
]