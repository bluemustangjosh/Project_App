from django.urls import path
from .views import landing, home, login_view, class_list_view, add_class_view

urlpatterns = [
    path('', landing, name='landing'),         
    path('login/', login_view, name='login'),   
    path('home/', home, name='home'),           
    path('classes/', class_list_view, name='class_list'),
    path('add_class/', add_class_view, name='add_class'),
]
