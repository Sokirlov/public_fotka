from django.urls import path, include
from .views import *
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'operations', views.OperationsAllApiView)
router.register(r'category', views.CategoryViewSet)

app_name = 'home_buh'

urlpatterns = [
    # path('all/', OperationsAllFreeApiView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('data-filter/', OperationDateView.as_view()),


]