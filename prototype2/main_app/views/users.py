from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main_app.models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class RegisterUserView(APIView):
    """
    Vista para registrar nuevos usuarios.
    """

    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')
        role = request.data.get('role', 'user')

        if not email or not username or not password:
            return Response({'error': 'Email, username, and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'A user with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User(
            email=email,
            username=username,
            password=make_password(password),
            role=role
        )
        user.save()

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    """
    Invalida el token refresh para realizar logout.
    """
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()  # Marca el token como inválido
            return Response({'message': 'Logout successful'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
