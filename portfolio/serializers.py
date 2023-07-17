from rest_framework import serializers
from .models import Portfolio, Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('title',)

class PortfolioSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Portfolio
        fields = ('title', 'categories', 'image', 'get_absolute_url')