from django.urls import include, path
from rest_framework import routers

from .views import (
    SchoolViewset,
    TeacherEndpoint,
    StudentEndpoint,
    SchoolTeacherEndpoint,
    SchoolStudentEndpoint,
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
    path("teachers/<int:pk>/", TeacherEndpoint.as_view()),
    path("schools/<int:pk>/teachers/", SchoolTeacherEndpoint.as_view()),
    # student related endpoints
    path("students/<int:pk>/", StudentEndpoint.as_view()),
    path("schools/<int:pk>/students/", SchoolStudentEndpoint.as_view()),
    #
]
