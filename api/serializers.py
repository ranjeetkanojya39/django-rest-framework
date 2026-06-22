from rest_framework import serializers
from api.models import Company


# create a serializer for the company model

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields="__all__"