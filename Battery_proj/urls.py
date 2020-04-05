
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csv_upload/', include('battery.urls')),
    path('api/', include('api.urls')),

]
