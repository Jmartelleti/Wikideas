from rest_framework.response import Response
from rest_framework.serializers import Serializer
from  rest_framework.decorators import api_view

from .models import Wiki
from .serializers import Wikiideas #importacion de class 

@api_view(['GET'])
def getWIKI(request):
    Wiki = Wiki,objects.all()
    serializer = Wikiideas(wiki, many=True)
    return Response (serializer.data)

@api_view(['POST'])
def postWIKI(request):
    data=request.data
    Wiki = Wiki.objects.create(
        body=data['body']
    )    