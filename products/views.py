from rest_framework import generics, filters
from .serializers import ProductSerializer
from .models import Product


# Create your views here.
class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    search_fields = ['score', 'name', 'price']
    
    def get_queryset(self):
        if self.request.data:
            return Product.objects.all().order_by(self.request.data['order']).values()

        return Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
