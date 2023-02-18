from rest_framework.response import Response
from rest_framework.serializers import Serializer
from  rest_framework.decorators import api_view
from .models import wiki
from .serializers import Wikiideas #importacion de class 
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from braces.views import CsrfExemptMixin


class Object(CsrfExemptMixin, APIView):
    authentication_classes = []

    def post(self, request, format=None):
        return Response({'received data': request.data})

@api_view(['GET'])
def getWIKI(request):
    blog = wiki.objects.all()
    serializer = Wikiideas(blog, many=True)
    return Response (serializer.data)

@api_view(['POST'])
def postWIKI(request):
    data=request.data
    blog = wiki.objects.create(
        body=data['body']
    )
    serializer = Wikiideas(blog , many= False)
    return Response(serializer.data)

api_view(['PUT'])
def putWIKI(request,pk):
    data = request.data 
    blog = wiki.objects.get(id=pk)
    serializer = Wikiideas(instance=blog, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

api_view(['DELETE'])
def deleteWIKI(request,pk):
    blog = wiki.objects.get(id=pk)
    wiki.delete()
    return Response('Wiki eliminado ')


    
from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

