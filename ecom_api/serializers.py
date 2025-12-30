from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # We use SlugRelatedField so you can send/see the NAME of the category 
    # instead of just an ID number, while keeping it editable.
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'description', 
            'price', 
            'category', 
            'stock_quantity', 
            'image_url', 
            'created_date'
        ]
        # 'created_date' should always be read-only as it's set by the system
        read_only_fields = ['created_date']

    # --- PROFESSIONAL VALIDATION ---

    def validate_price(self, value):
        """Ensure the price is a positive number."""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_stock_quantity(self, value):
        """Ensure stock is not negative."""
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value

    def validate_name(self, value):
        """Ensure the product name is professional (not just numbers)."""
        if value.isdigit():
            raise serializers.ValidationError("Product name cannot be only numbers.")
        return value