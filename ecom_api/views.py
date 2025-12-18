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
    
    # This enables the search, filtering, and ordering features
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # This allows users to filter by category ID, category NAME, or price
    # Adding 'category__name' allows filtering by the actual name (e.g. ?category__name=Luxury Skincare)
    filterset_fields = ['category', 'category__name', 'price']
    
    # This allows users to search by product name or description
    search_fields = ['name', 'description']
    
    # This allows users to sort by price or date
    ordering_fields = ['price', 'created_date']