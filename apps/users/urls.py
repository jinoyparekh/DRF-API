from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

rt = routers.DefaultRouter()
routers.register(r'', UserViewSet)

urlpatterns = [
    path('', include(rt.urls)),
]
