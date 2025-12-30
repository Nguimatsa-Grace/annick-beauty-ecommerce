from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    # A slug is useful for URLs, though optional for this specific API
    slug = models.SlugField(max_length=120, unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    
    # DecimalField is correct for money. 
    # Added MinValueValidator so DB refuses negative prices.
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        db_index=True
    )
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='products'
    )
    
    # PositiveIntegerField prevents negative stock at the database level.
    stock_quantity = models.PositiveIntegerField(default=0)
    
    image_url = models.URLField(max_length=500, blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # Useful for tracking inventory updates

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name