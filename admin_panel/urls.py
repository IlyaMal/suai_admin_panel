from django.urls import path
 
from . import views

app_name = 'admin_panel'
 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]