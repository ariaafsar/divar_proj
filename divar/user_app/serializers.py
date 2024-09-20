from rest_framework import serializers
from .models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(max_length=12)
    location = serializers.CharField(max_length=255)
    
    class Meta:
        model = UserAccount
        fields = '__all__'
    
    def create(self , validated_data):
        user = UserAccount.objects.create(
            phone_number = validated_data['phone_number'],
            location = validated_data['location'],
            user = validated_data['user']
        )   start
        return user
    