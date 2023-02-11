from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import BasePermission

# Create your views here.
class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [BasePermission]

    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [BasePermission]

    serializer_class = UserSerializer
    queryset = User.objects.all()
