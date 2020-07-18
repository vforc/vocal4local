import json

from django.shortcuts import render
from django.http import  HttpResponse
from .models import Company
import wikipedia
from http import HTTPStatus


def companyInfo(request,company_name):
    company = Company.objects.filter(pk=company_name)
    response_data = dict()
    response_data['company_name'] = company_name
    if company:
        response_data['isIndian'] = company.isIndian
    else:
        try:
            company_summary = wikipedia.summary(company)
        except Exception as e:
            company_summary = None
        if company_summary:
            if "is an Indian" in company_summary:
                isIndian = True
            else:
                isIndian = False
            company = Company.objects.create(companyName=company_name, isIndian=isIndian, companySummary=company_summary)
        else:
            company = Company.objects.create(companyName=company_name, isIndian=False, companySummary="Not Found")
        response_data['isIndian'] = company.isIndian
    return HttpResponse(status=HTTPStatus.ACCEPTED, data=json.dumps(response_data), content_type="application/json")


def companyInfoList(request, company_names):
    response_data = dict()
    for company_name in company_names:
        company = Company.objects.filter(pk=company_name)
        if company_name not in response_data:
            response_data['company_name'] = company_name
        if company:
            response_data['isIndian'] = company.isIndian
        else:
            try:
                company_summary = wikipedia.summary(company)
            except Exception as e:
                company_summary = None
            if company_summary:
                if "is an Indian" in company_summary:
                    isIndian = True
                else:
                    isIndian = False
                company = Company.objects.create(companyName=company_name, isIndian=False, companySummary=company_summary)
            else:
                company = Company.objects.create(companyName=company_name, isIndian=False, companySummary="Not Found")
            response_data['isIndian'] = company.isIndian
    return HttpResponse(status=HTTPStatus.ACCEPTED, data=json.dumps(response_data), content_type="application/json")