from rest_framework import permissions
from student.models import Student

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import StudentSerializers

# Create your views here.


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = (IsAuthenticated,)
