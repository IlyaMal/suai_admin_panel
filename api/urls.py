from django.urls import path
 
from . import views

app_name = 'api'
 
urlpatterns = [
    path('users/', views.UserListApiView.as_view()),
    path('users/create/', views.UserCreateApiView.as_view()),
    path('users/<int:pk>/', views.UserRetrieveAPIView.as_view()),
    path('queries/', views.QueryListApiView.as_view()),
    path('queries/create/', views.QueryCreateApiView.as_view()),
    path('queries/<int:pk>/', views.QueryRetrieveAPIView.as_view()),
    path('offices/working_days/<int:office_id>/', views.WorkingDayListAPIView.as_view())
]