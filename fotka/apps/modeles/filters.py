from .models import Modeles
import django_filters

class ModelesAllViewFilter(django_filters.FilterSet):
    class Meta:
        model = Modeles
        fields = ['sex', 'money',]