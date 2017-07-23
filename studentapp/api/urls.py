from django.conf.urls import include, url
from rest_framework import routers
from viewsets import * 
from views import add_student
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register('student',StudentViewSet)

urlpatterns = [
		url(r'^',include(router.urls)),
		url(r'student/add$',add_student.as_view()),		
]	