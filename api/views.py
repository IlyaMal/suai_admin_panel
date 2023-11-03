from rest_framework import views, generics
from rest_framework.response import Response
from admin_panel.models import User, Query
from .serializers import UserSerializer, QuerySerializer


class UserApiView(views.APIView):
    def get(self, args, **kwargs):
        users = User.objects.all().values()
        return Response(UserSerializer(users, many=True).data)
    
    def post(self, request):
        serializer: UserSerializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    

class QueryListApiView(generics.ListAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer