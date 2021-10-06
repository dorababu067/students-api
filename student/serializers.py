from .models import Student, School, Teacher

from django.contrib.auth.models import User

from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentDetailSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = ["id", "name", "age", "address", "phone", "school"]


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherDetailSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField()

    class Meta:
        model = Teacher
        fields = [
            "id",
            "name",
            "age",
            "qualification",
            "subjects",
            "role",
            "address",
            "phone",
            "bio",
            "school",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "groups", "user_permissions"]
