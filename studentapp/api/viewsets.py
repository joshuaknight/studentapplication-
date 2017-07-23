from rest_framework import viewsets
import serializers
import models 


class StudentViewSet(viewsets.ModelViewSet):
		queryset = models.StudentModel.objects.all()	
		serializer_class = serializers.StudentSerializer			