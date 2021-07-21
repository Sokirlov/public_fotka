from rest_framework import serializers
from .models import Modeles


class ModelesAllFreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modeles
        fields = ['fio', 'tel', 'email', 'insta', 'fb', 'face', 'full_photo', 'sex', 'birthday', 'lenth', 'weight', 'chest', 'waist', 'hips', 'footwear', 'hair_color', 'haer_lenth', 'money', 'tfp',]

