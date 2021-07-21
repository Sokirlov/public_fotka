from rest_framework import serializers
from .models import Operations, Categories
from .models import userProfile
from django.contrib.auth.models import User, Group



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=userProfile
        fields='__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class OperationsAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = ['id', 'opertime', 'name', 'categoryId', 'operations', 'summa', 'owner', ]

class OperationCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'categoryName', 'operations']