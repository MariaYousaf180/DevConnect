from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeveloperProfileViewSet

router = DefaultRouter()
router.register(r'developers' , DeveloperProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
# connect/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeveloperProfileViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'developers', DeveloperProfileViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

