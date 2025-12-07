from django.contrib import admin
from django.urls import path
from MargemPredict import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.simular_nf, name='simular_nf'),
]
