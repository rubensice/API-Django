from .models import *
from .serializers import *
from rest_framework.views import APIView, ModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class CharacterAPIView(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

class LocationAPIView(APIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    
class EpisodeAPIView(APIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    