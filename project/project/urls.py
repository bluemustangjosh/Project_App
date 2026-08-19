from django.contrib import admin
from django.urls import path, include
from testApp.views import landing

urlpatterns = [
    path('', landing, name='landing'),
    path('admin/', admin.site.urls),

    # login app MUST be included
    path('login/', include('login.urls')),

    # classes
    path('classes/', include('classes.urls')),

    # testApp last because it catches root-level routes
    path('', include('testApp.urls')),
]
