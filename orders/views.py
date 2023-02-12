from rest_framework import generics
from rest_framework.views import status, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import OrderSerializer
from .models import Order
import ipdb

# Create your views here.
class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    authentication_classes = [JWTAuthentication]

    def get_queryset(self):

        if not self.request.user.is_anonymous:
            return Order.objects.filter(buyer=self.request.user)

        return Order.objects.all()

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)

        serializer.save(buyer=self.request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
