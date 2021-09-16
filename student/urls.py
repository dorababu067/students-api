from django.urls import include, path
from rest_framework import routers

from .views import StudentViewset

router = routers.DefaultRouter()
router.register(r"students", StudentViewset, basename="students")

urlpatterns = [
    path("", include(router.urls)),
]
