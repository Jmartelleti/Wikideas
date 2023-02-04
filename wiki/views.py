from rest_framework.response import Response
from rest_framework.serializers import Serializer
from  rest_framework.decorators import api_view

from .models import Wiki
from .serializers import Wikiideas #importacion de class 

@api_view(['GET'])
def getWIKI(request):
    Wiki = Wiki.objects.all()
    serializer = Wikiideas(Wiki, many=True)
    return Response (serializer.data)

@api_view(['POST'])
def postWIKI(request):
    data=request.data
    Wiki = Wiki.objects.create(
        body=data['body']
    )
    serializer = Wikiideas(Wiki , many= False)
    return Response(serializer.data)

api_view(['PUT'])
def putWIKI(request,pk):
    data = request.data 
    wiki = Wiki.objects.get(id=pk)
    serializer = Wikiideas(instance = Wiki , data= data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

api_view(['DELETE'])
def deleteWIKI(request,pk):
    Wiki = Wiki.objects.get(id=pk)
    Wiki.delete()
    return Response('Wiki eliminado ')