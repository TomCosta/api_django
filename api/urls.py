from django.urls import path
from .views import ListNoteView


urlpatterns = [
    path('note/', ListNoteView.as_view(), name="note-all")
]