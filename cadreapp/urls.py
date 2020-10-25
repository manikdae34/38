from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('load-district', views.load_district, name='load-district'),
    
]