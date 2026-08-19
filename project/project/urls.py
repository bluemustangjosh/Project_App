from django.contrib import admin
from django.urls import path, include
from testApp.views import landing

urlpatterns = [
    path('', landing, name='landing'),
    path('admin/', admin.site.urls),

    # MOVE THIS ABOVE testApp
    path('classes/', include('classes.urls')),

    # This must be LAST because it catches everything
    path('', include('testApp.urls')),
]
