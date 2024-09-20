from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView , ListAPIView
from .models import UserAccount
from .serializers import UserAccountSerializer
from rest_framework import status


class UserCreate(CreateAPIView):
    serializer_class = UserAccountSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_account = UserAccount.objects.create(user = user , phone_number = request.data['phone_number'], location=request.data['location'])
        return Response({'message': 'New user successfully created'}, status=status.HTTP_201_CREATED)
    


# Create your views here