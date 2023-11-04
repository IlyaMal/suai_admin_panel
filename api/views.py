from rest_framework import views, generics
from rest_framework.response import Response
from admin_panel.models import User, Query
from .serializers import UserSerializer, QuerySerializer


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