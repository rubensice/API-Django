from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class CharacterAPIView(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class LocationAPIView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
class EpisodeAPIView(ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    