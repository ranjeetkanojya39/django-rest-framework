
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serializers import CompanySerializer




class CompanyViewsets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer