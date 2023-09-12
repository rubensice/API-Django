from .models import *
from .serializers import *
from rest_framework.views import APIView, ModelViewSet
from rest_framework.response import Response


class CharacterAPIView(APIView):
    def get(self, request, characterId = ''):
        #se o get não tiver o filtro de id:
        if characterId == '':
            characterFound = ''
            if 'name' in request.GET and 'status' in request.GET:
                #pegando o parametro que foi informado!
                nameToFilter = request.GET['name']
                statusToFilter = request.GET['status']
                #characterFound = Character.objects.filter(name__contains=nameToFilter).filter(status__contains=statusToFilter)
                characterFound = Character.objects.filter(name__contains=nameToFilter) | Character.objects.filter(status__contains=statusToFilter)
            elif 'name' in request.GET:
                #pegando o parametro que foi informado!
                nameToFilter = request.GET['name']
                characterFound = Character.objects.filter(name__contains=nameToFilter)
            elif 'status' in request.GET:
                #pegando o parametro que foi informado!
                statusToFilter = request.GET['status']
                characterFound = Character.objects.filter(status__contains=statusToFilter)
            else:
                characterFound = Character.objects.all() #select *from people;
            serializer = CharacterSerializer(characterFound, many=True)
            return Response(status= 200, data = serializer.data) #busca por people id:
    #busca por people id:
        try:
            characterFound = Character.objects.get(id=characterId) #select *from people;
            serializer = CharacterSerializer(characterFound, many=False)
            return Response(serializer.data) #busca por people id:
        except Character.DoesNotExist:
            return Response(status=404, data="character not found")


    #select *from people where id = peopleId
    def post(self, request):
        #pega o json do cliente e guardando na variable
        characterJson = request.data
        #convertendo o json em phyton
        characterSerialized = CharacterSerializer(data=characterJson, many=False)
        #verificar se os dados estão coerentes
        if characterSerialized.is_valid():
            #salvando no banco de dados
            characterSerialized.save()
            return Response(status=201, data=characterSerialized.data)
        return Response(status=400, data="mande certo seu imbecil!")
    

    def delete(self, request, characterId= ''):

        if(characterId != ''):
            #procurar a pessoa com o id!
            characterFound = Character.objects.get(id=characterId)
            #deletando o usuario encontrado!
            characterFound.delete()
            return Response(status=200, data='Character sucessfully deleted!')
        
        return Response(status=400, data= 'characterId must be given')
    
    def put(self, request, characterId = ''):

        if(characterId != ''): 
            #procurar o antigo:
            characterFound = Character.objects.get(id=characterId)

            #coletar o novo que veio JSON:
            characterToUpdateJSON = request.data

            #faz o serializer substituir o novo pelo antigo e converter em python
            serializedCharacter = CharacterSerializer(characterFound, data=characterToUpdateJSON)

            #verificar se a conversao é valida
            if(serializedCharacter.is_valid()):
                #salvo no banco de dados
                serializedCharacter.save()
                return Response(status=200, data=serializedCharacter.data)
            return Response(status=400, data='Invalid data!')

class LocationAPIView(APIView):
    def get(self, request, locationId = ''): 
        if locationId == '':
            locationFound = Location.objects.all() #select *from planet;
            serializer = LocationSerializer(locationFound, many=True)
            return Response(serializer.data)
    #busca por people id:
        try:
            locationFound = Location.objects.get(id=locationId) #select *from people where id = peopleId
            serializer = LocationSerializer(locationFound, many=False) #JSON
            return Response(serializer.data)
        except Location.DoesNotExist:
            return Response(status=404, data="Location not found")


    def post(self, request):
        #pega o json do cliente e guardando na variable
        locationJson = request.data
        #convertendo o json em phyton
        locationSerialized = LocationSerializer(data=locationJson, many=False)
        #verificar se os dados estão coerentes
        if locationSerialized.is_valid():
            #salvando no banco de dados
            locationSerialized.save()
            return Response(status=201, data=locationSerialized.data)
        return Response(status=400, data="mande certo seu imbecil!")
    

    def delete(self, request, locationId= ''):

        if(locationId != ''):
            #procurar a pessoa com o id!
            locationFound = Location.objects.get(id=locationId)
            #deletando o usuario encontrado!
            locationFound.delete()
            return Response(status=200, data='Location sucessfully deleted!')
        
        return Response(status=400, data= 'locationId must be given')
    
    def put(self, request, locationId = ''):

        if(locationId != ''): 
            #procurar o antigo:
            locationFound = Location.objects.get(id=locationId)

            #coletar o novo que veio JSON:
            locationToUpdateJSON = request.data

            #faz o serializer substituir o novo pelo antigo e converter em python
            serializedLocation = LocationSerializer(locationFound, data=locationToUpdateJSON)

            #verificar se a conversao é valida
            if(serializedLocation.is_valid()):
                #salvo no banco de dados
                serializedLocation.save()
                return Response(status=200, data=serializedLocation.data)
            return Response(status=400, data='Invalid data!')
    

class EpisodeAPIView(APIView):
    def get(self, request, episodeId = ''):
        if episodeId == '':
            episodeFound = Episode.objects.all()
            serializer = EpisodeSerializer(episodeFound, many=True)
            return Response(serializer.data)
    #busca por people id:
        try:
            episodeFound = Episode.objects.get(id=episodeId) #select *from planet;
            serializer = EpisodeSerializer(episodeFound, many=False)
            return Response(serializer.data)
        except Episode.DoesNotExist:
            return Response(status=404, data="Episode not found")


    def post(self, request):
        #pega o json do cliente e guardando na variable
        episodeJson = request.data
        #convertendo o json em phyton
        episodeSerialized = EpisodeSerializer(data=episodeJson, many=False)
        #verificar se os dados estão coerentes
        if episodeSerialized.is_valid():
            #salvando no banco de dados
            episodeSerialized.save()
            return Response(status=201, data=episodeSerialized.data)
        return Response(status=400, data="mande certo seu imbecil!")
    

    def delete(self, request, episodeId= ''):

        if(episodeId != ''):
            #procurar a pessoa com o id!
            episodeFound = Episode.objects.get(id=episodeId)
            #deletando o usuario encontrado!
            episodeFound.delete()
            return Response(status=200, data='Episode sucessfully deleted!')
        
        return Response(status=400, data= 'episodeId must be given')
    
    def put(self, request, episodeId = ''):

        if(episodeId != ''): 
            #procurar o antigo:
            episodeFound = Episode.objects.get(id=episodeId)

            #coletar o novo que veio JSON:
            episodeToUpdateJSON = request.data

            #faz o serializer substituir o novo pelo antigo e converter em python
            serializedEpisode = EpisodeSerializer(episodeFound, data=episodeToUpdateJSON)

            #verificar se a conversao é valida
            if(serializedEpisode.is_valid()):
                #salvo no banco de dados
                serializedEpisode.save()
                return Response(status=200, data=serializedEpisode.data)
            return Response(status=400, data='Invalid data!')