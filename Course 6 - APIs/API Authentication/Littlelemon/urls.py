from django.contrib import admin
from django.urls import path, include
from LittleLemonAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('LittleLemonAPI.urls'))
]