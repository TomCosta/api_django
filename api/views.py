from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer


class ListNoteView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
