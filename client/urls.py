# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from client import views

router = DefaultRouter()
router.register(r'clients', views.ClientViewSet, basename='clients')

urlpatterns = [
    path('', include(router.urls))
]