from .models import Operations, Categories
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from home_buh.serializers import UserSerializer, GroupSerializer, OperationsAllSerializer, OperationCategorySerializer
import django_filters
from django_filters.rest_framework import DjangoFilterBackend


class OperationFilter(django_filters.FilterSet):
    opertime = django_filters.DateFromToRangeFilter(field_name='opertime', label='Filter to (yyyy-mm-dd):')
    class Meta:
        model = Operations
        fields = [
            "opertime",
        ]




class OperationsAllApiView(viewsets.ModelViewSet):
    queryset = Operations.objects.all().order_by('-opertime')
    serializer_class = OperationsAllSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_class = OperationFilter

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(owner=self.request.user)
        return query_set

    def perform_create(self, serializer):
        kwargs = {
            'owner': self.request.user
        }
        serializer.save(**kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = OperationCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class OperationDateView(APIView):
    def get(self, request):
        query_date_from = request.GET.get('date_from')
        query_date_to = request.GET.get('date_to')
        query_operations = request.GET.get('operations')
        query_categoryId = request.GET.get('categoryId')
        if query_date_to == None:
            snippets = Operations.objects.all()
        else:
            date_to = str(query_date_to)
            date_from = str(query_date_from)
            snippets = Operations.objects.all().filter(opertime__range=[date_from, date_to])
        if query_operations == None:
            snippets = snippets
        else:
            operations = str(query_operations)
            snippets = snippets.filter(operations=operations)

        if query_categoryId == None:
            snippets = snippets
        else:

            snippets = snippets.filter(categoryId=query_categoryId)

        serializer = OperationsAllSerializer(snippets, many=True)
        return Response(serializer.data)