#project urls.py
from django.contrib import admin
from django.urls import path, include
from testApp.views import landing

urlpatterns = [
    path('', landing, name='landing'),
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('classes/', include('classes.urls')),
    path('home/', include('home.urls')),

    # testApp last because it catches root-level routes
    path('', include('testApp.urls')),
]