from rest_framework import serializers
from models import StudentModel

class StudentSerializer(serializers.
		HyperlinkedModelSerializer):
	class Meta:
		model = StudentModel
		fields = ('id','name','age','gender','roll_no','url')		

