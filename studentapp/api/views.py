

from django.http import request,JsonResponse,HttpResponse
from django.shortcuts import render 
from models import StudentModel
from serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import pagination 
from rest_framework.response import Response

class add_student(generics.CreateAPIView):
	    queryset = StudentModel.objects.all()
	    serializer_class = StudentSerializer
