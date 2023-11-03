from rest_framework import serializers
from admin_panel.models import User, Query


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'

    # def create(self, validated_data):
    #     return Query.objects.create(**validated_data)