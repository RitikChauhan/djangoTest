import json

from django.shortcuts import render
from rest_framework import *
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from app.models import Company, Employee
from app.serializers import CompanySerializer, EmployeeSerializer


# Create your views here.

class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        sector = request.data.get("sector")
        is_active = request.data.get("is_active")

        Company.objects.create(name=name, sector=sector, is_active=is_active,)

        return Response(status=status.HTTP_201_CREATED)


class CompanyGetView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Company.objects.filter(id=kwargs.get("pk"), sector=kwargs.get("sector"))

        data_list = []
        for data in queryset:
            data_dump = {
                "name": data.name,
                "sector": data.sector,
                "is_active": data.is_active
            }
            data_list.append(data_dump)

        return Response(data=data_list, status=status.HTTP_200_OK, content_type="application/json")


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        salary = request.data.get("salary")
        company_id = request.data.get("company_id")

        if not company_id:
            return Response(status=status.HTTP_400_BAD_REQUEST, data = {"msg": "company_id must be present in the body"})

        Employee.objects.create(name=name, salary=salary, company_id=company_id)

        return Response(status=status.HTTP_201_CREATED)


