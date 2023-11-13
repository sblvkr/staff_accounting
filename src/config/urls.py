from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('staff.urls', namespace='staff')),
    path('admin/', admin.site.urls),
]
