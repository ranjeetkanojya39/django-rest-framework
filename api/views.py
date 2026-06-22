
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company , Employee
from api.serializers import CompanySerializer,EmployeeSerializer




class CompanyViewsets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewsets(viewsets.ModelViewSet):
    queryset  =  Employee.objects.all()
    serializer_class=EmployeeSerializer