from django.urls import path
from . import views
# from .views import ModelesAllView
app_name = 'modeles'

urlpatterns =(
    # path('', ModelesView.as_view(), name='modele'),
    path('', views.ModelesView, name='modele'),
    # path('login/',  'django.contrib.auth.views.login', name='login'),
    # path('logout/', 'django.contrib.auth.views.logout', name='logout'),
    # path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    path('all/', views.ModelesAllView, name='modeles_list'),
)