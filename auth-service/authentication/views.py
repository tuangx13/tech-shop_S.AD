from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .utils import generate_jwt_token, verify_token


@api_view(['POST'])
def register(request):
    """Register a new user"""
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        token = generate_jwt_token(user)

        return Response({
            'message': 'User registered successfully',
            'user': UserSerializer(user).data,
            'token': token
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    """Login user and return JWT token"""
    serializer = LoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    role = serializer.validated_data.get('role')

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    # Verify role if provided
    if role and user.role != role:
        return Response({'error': f'User is not a {role}'}, status=status.HTTP_403_FORBIDDEN)

    token = generate_jwt_token(user)

    return Response({
        'message': 'Login successful',
        'user': UserSerializer(user).data,
        'token': token
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def verify(request):
    """Verify JWT token"""
    payload = verify_token(request)

    if payload is None:
        return Response({'error': 'Invalid or expired token'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = User.objects.get(id=payload['user_id'])
        return Response({
            'valid': True,
            'user': UserSerializer(user).data
        }, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def me(request):
    """Get current user info"""
    payload = verify_token(request)

    if payload is None:
        return Response({'error': 'Invalid or expired token'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = User.objects.get(id=payload['user_id'])
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
