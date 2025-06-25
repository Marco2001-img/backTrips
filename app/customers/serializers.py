from rest_framework import serializers,viewsets, status
from .models import Cliente
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # Puedes cambiarlo



class ClienteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, min_length=6)

    class Meta:
        model = Cliente
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'password', 'address']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Cliente.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
    