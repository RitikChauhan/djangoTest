from django.urls import path

from app.views import CompanyCreateView, CompanyGetView, EmployeeCreateView

urlpatterns = [
    path("companies/create", CompanyCreateView.as_view()),
    path('companies/<pk>/<sector>/fetch', CompanyGetView.as_view()),
    path("employee/create", EmployeeCreateView.as_view())
]