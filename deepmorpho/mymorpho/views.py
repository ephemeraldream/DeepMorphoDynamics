from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Images, ImageWithClassificationPredictions
from .serializers import ImagesSerializer, ClassificationSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

def members(request):
    return HttpResponse("Hello world!")
# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [AllowAny]

class ClassedImsViewSet(viewsets.ModelViewSet):
    queryset = ImageWithClassificationPredictions.objects.all()
    serializer_class = ClassificationSerializer
    permission_classes = [AllowAny]

@api_view(['GET'])
def getData(request):
    person = {'name': 'Dennis', 'age': 28}
    return Response(person)





