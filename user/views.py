from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from .serializers import UserSerializer, GroupSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if not username or not password or not email:
        return Response({'error':'Please provide all required credentials.'})
    if User.objects.filter(email = email).exists():
        return Response({'error':'User with this email already exists.'})
    else:
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )
        return Response({'message':'User registered successfully.'})
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        print(f"User {user.username} authenticated successfully.")
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    else:
        print(f"Authentication failed for email: {email}")
        return Response({'error': 'Invalid credentials'})
    
@api_view(['POST'])
@permission_classes([AllowAny])

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({'message': 'Logged out successfully'})
    else:
        return Response({'error': 'User is not logged in'})
    

@api_view(["GET"])

def grouplist(request):
    group_objs = Group.objects.all().exclude(name = 'Owner')
    serializer = GroupSerializer(group_objs, many = True)
    return Response (serializer.data)
    
    
