from rest_framework import serializers
from .models import *

#vai converter o python dos models em json p/ a api
class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Character
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
        class Meta:
            many = True
            model = Location
            fields = '__all__'

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Episode
        fields = '__all__' 
