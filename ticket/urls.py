from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ticket.urls')),  # change 'your_app_name' accordingly
    
]
