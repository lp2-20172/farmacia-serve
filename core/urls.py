from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet
from .views import PersonViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
