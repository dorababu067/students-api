from django.urls import include, path
from rest_framework import routers

from .views import (
    SchoolViewset,
    SchoolTeacherEndpoint,
    ShoolTeacherDetailEndpoint,
    SchoolStudentEndpoint,
    SchoolStudentDetailEndpoint,
)


urlpatterns = [
    # school related endpoints
    path("schools/", SchoolViewset.as_view({"get": "list", "post": "create"})),
    path(
        "schools/<int:pk>/",
        SchoolViewset.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    #
    # teachers related endpoints
    path("schools/<int:pk>/teachers/", SchoolTeacherEndpoint.as_view()),
    path(
        "schools/<int:school_id>/teachers/<int:teacher_id>/",
        ShoolTeacherDetailEndpoint.as_view(),
    ),
    # student related endpoints
    path("schools/<int:pk>/students/", SchoolStudentEndpoint.as_view()),
    path(
        "schools/<int:school_id>/students/<int:student_id>/",
        SchoolStudentDetailEndpoint.as_view(),
    ),
    #
]
