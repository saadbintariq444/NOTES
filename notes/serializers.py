from rest_framework import serializers
from . import models

# a serializer will convert json data of model data base to json response data

class NoteSerializer(serializers.ModelSerializer):
    
 class Meta:
    model = models.Note
    fields= '__all__'
        