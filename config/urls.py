from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('frontend_demo/', include('frontend_demo.urls')), 
    path('visit/', include('visitcounter.urls')),
]