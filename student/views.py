from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

from student.models import Student, School, Teacher
from .serializers import (
    StudentSerializer,
    StudentDetailSerializer,
    SchoolSerializer,
    TeacherDetailSerializer,
    TeacherSerializer,
    TeacherDetailSerializer,
    UserSerializer,
)

# Create your views here.


class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (IsAuthenticated,)


class TeacherEndpoint(APIView):
    def get_teacher(self, teacher_id):
        try:
            school = Teacher.objects.get(id=teacher_id)
            return school
        except School.DoesNotExist:
            raise serializers.ValidationError(
                {"error": "please provide valid teacher id"}
            )

    def get(self, request, pk):
        teacher = self.get_teacher(pk)
        serializer = TeacherDetailSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = self.get_teacher(pk)
        serializer = TeacherSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        teacher = self.get_teacher(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SchoolObjectMixin(object):
    def get_school(self, school_id):
        try:
            school = School.objects.get(id=school_id)
            return school
        except School.DoesNotExist:
            raise serializers.ValidationError(
                {"error": "please provide valid school id"}
            )


class SchoolTeacherEndpoint(SchoolObjectMixin, APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        school = self.get_school(pk)
        queryset = Teacher.objects.filter(school_id=school.id)
        serializer = TeacherSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        school = self.get_school(pk)
        request.data["school"] = school.id
        serializer = TeacherSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)


class SchoolStudentEndpoint(SchoolObjectMixin, APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        school = self.get_school(pk)
        queryset = Student.objects.filter(school__id=school.id)
        serializer = StudentDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        school = self.get_school(pk)
        request.data["school"] = school.id
        serializer = StudentSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            # new student
            serializer.save()
            return Response(serializer.data)


class StudentEndpoint(APIView):
    def get_student(self, student_id):
        try:
            student = Student.objects.get(id=student_id)
            return student
        except Student.DoesNotExist:
            raise serializers.ValidationError(
                {"error": "please provide valid student id"}
            )

    def get(self, request, pk):
        student = self.get_student(pk)
        serializer = StudentDetailSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_student(pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        student = self.get_student(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserEndpoint(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data.get("password"))
            user.save()
            jwt_token = get_tokens_for_user(user)
            jwt_token["username"] = request.data.get("username")
            jwt_token["email"] = request.data.get("email")
            return Response(jwt_token)


class UserDetailEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
