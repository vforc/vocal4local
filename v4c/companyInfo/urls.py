
from django.urls import path

from . import views

app_name = 'companyInfo'
urlpatterns = [
    path('company/<str:pk>/', views.companyInfo),
    path('companies/(?P<company_list>\w+)/', views.companyInfoList),
]