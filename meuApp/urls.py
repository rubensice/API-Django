#biblioteca p/ trabalhar com as rotas/endpoints
from django.urls import path

#importando tudo o que tem nas nossas views
from .views import *

urlpatterns = [
    path('character/', CharacterAPIView.as_view(), name="character"),
    path('character/<int:characterId>', CharacterAPIView.as_view(), name="characterById"),
    path('location/', LocationAPIView.as_view(), name="location"),
    path('location/<int:locationId>', LocationAPIView.as_view(), name="locationById"),
    path('episode/', EpisodeAPIView.as_view(), name="episode"),
    path('episode/<int:episodeId>', EpisodeAPIView.as_view(), name="episodeById"),
]

