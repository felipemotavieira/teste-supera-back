from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import OrderSerializer
from .models import Order
import ipdb

# Create your views here.
class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
