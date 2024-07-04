from rest_framework import serializers
from .models import Area,Company,Building



class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['name', 'author']


class CompanyTashkilotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'