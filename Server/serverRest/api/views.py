from django.shortcuts import render

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Example
from .serializers import BaseExampleSerializer

@api_view(['GET'])
def helloApi(request):
    return Response("Hello World!")

@api_view(['GET'])
def exampleAPI(request, id):
    result = Example.objects.get(id = id)
    serializer = BaseExampleSerializer(result)
    return Response("Example test")