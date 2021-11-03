from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Text

User=get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['username','password','email','password2']
    def save(self):
        reg = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password !=password2:
            raise serializers.ValidationError({'password':'Password does not match'})
        reg.set_password(password)
        reg.save()
        return reg
    
class TextSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    timestamp = serializers.DateTimeField()
    user = serializers.CharField(max_length=200)

    class Meta:
        model = Text
        fields = ('__all__')