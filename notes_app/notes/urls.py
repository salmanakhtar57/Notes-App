from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotesViewSet

#DRF routers automatically generate URL patterns for your ViewSets.

router = DefaultRouter()
router.register(r'notes', NotesViewSet)

urlpatterns = [
    path('', include(router.urls))
]