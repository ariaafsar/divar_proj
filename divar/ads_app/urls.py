from django.urls import path
from .views import AddAds , AdsList

urlpatterns = [
path('create' , AddAds.as_view()),
path('list' , AdsList.as_view()),
]