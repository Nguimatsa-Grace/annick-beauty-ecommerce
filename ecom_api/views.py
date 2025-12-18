from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # This enables the search and filtering features
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # This allows users to filter by category or price
    filterset_fields = ['category', 'price']
    
    # This allows users to search by product name
    search_fields = ['name']
    
    # This allows users to sort by price or date
    ordering_fields = ['price', 'created_date']