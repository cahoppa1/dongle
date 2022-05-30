from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from .models import Table
# Create your views here.

class APIResponseView(APIView):
    def get(self, request):
        content = [case.casename for case in Table.Objects.all()]
        return Response(content)


