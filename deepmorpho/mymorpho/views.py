from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Images
from .serializers import ImagesSerializer

def members(request):
    return HttpResponse("Hello world!")
# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer




