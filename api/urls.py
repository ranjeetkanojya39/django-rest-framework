from django.contrib import admin
from django.urls import path , include
from api.views import CompanyViewsets
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'companies', CompanyViewsets)


urlpatterns = [
    path('' , include(router.urls))
]




