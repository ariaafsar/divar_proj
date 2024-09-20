from django.shortcuts import render
from .models import Ad
from user_app.models import UserAccount
from .serializers import AdSerializer
from rest_framework.generics import CreateAPIView , ListAPIView
class AddAds(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    
class AdsList(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

# Create your views here.
