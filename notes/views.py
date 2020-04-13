from rest_framework import generics
from . import models
from . import serializers 

# Create your views here.
# NoteList(generics.ListAPIView)
class NoteList(generics.ListCreateAPIView):
    queryset = models.Note.objects.all().order_by('-created_at', '-updated_at')
    serializer_class = serializers.NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer