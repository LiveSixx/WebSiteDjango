from django.urls import path, include
from . import views


app_name = 'siteServices'
urlpatterns = [
    path('', views.services, name='services'),
    path('<int:service_id>/', views.service_detail, name='service_detail')
]