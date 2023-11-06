from rest_framework import generics, views
from admin_panel.models import User, Query, WorkingDay
from .serializers import UserSerializer, QuerySerializer, WorkingDaySerializer
from rest_framework.response import Response


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QueryCreateApiView(generics.CreateAPIView):
    serializer_class = QuerySerializer


class QueryListApiView(generics.ListAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class QueryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class WorkingDayListAPIView(generics.ListAPIView):
    serializer_class = WorkingDaySerializer

    def get_queryset(self):
        office_id = self.kwargs['office_id']
        return WorkingDay.objects.filter(office=office_id)