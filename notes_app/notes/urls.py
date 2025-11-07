from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#DRF routers automatically generate URL patterns for your ViewSets.

# router = DefaultRouter()
# router.register(r'notes', NotesViewSet)

urlpatterns = [
    path('notes/', views.notes_list_create, name="notes-list-create"),
    path('notes/<int:pk>', views.notes_detail, name='note-detail')
]