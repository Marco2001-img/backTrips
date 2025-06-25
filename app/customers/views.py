from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import ClienteSerializer
from rest_framework.views import APIView
from rest_framework import status
from .models import Cliente
from rest_framework import viewsets


class RegisterView(APIView):
    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Cliente registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]  # Sólo usuarios autenticados pueden ver/modificar clientes

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]  # Permite crear sin autenticación (registro)
        return super().get_permissions()