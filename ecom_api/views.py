from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class ProductFilter(django_filters.FilterSet):
    """
    Custom filter class to handle advanced requirements like Price Range 
    and Stock Availability.
    """
    # Price range filters
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    
    # Category filters (by ID or by Name)
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    category_name = django_filters.CharFilter(field_name="category__name", lookup_expr='icontains')
    
    # Stock Availability: Returns only items where stock is > 0
    in_stock = django_filters.BooleanFilter(method='filter_in_stock', label="In Stock Only")

    class Meta:
        model = Product
        fields = ['category', 'category_name', 'min_price', 'max_price']

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock_quantity__gt=0)
        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # Filter Backends
    filter_backends = [
        django_filters.DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    
    # Use the custom filter class we created above
    filterset_class = ProductFilter
    
    # Partial matching search (name or description)
    search_fields = ['name', 'description']
    
    # Sorting options
    ordering_fields = ['price', 'created_date', 'stock_quantity']
    ordering = ['-created_date']  # Default: newest products first