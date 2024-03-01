from django.contrib.auth.models import User

from rest_framework import serializers

from api.models import Product,BasketItem,Basket


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']
        read_only_fields=['id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        read_only_fields=['id','category']
    
    category=serializers.StringRelatedField()

class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=BasketItem
        fields='__all__'
        read_only_fields=['id','basket','product','is_active','created_at','updated_at','total']
        
    product=ProductSerializer(read_only=True)
    total=serializers.IntegerField(read_only=True)

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Basket
        fields='__all__'
        read_only_fields=['id','owner','created_at','is_active','updated_at','cart_items']
    
    basket_item_total=serializers.IntegerField(read_only=True)
    cart_items=BasketItemSerializer(read_only=True,many=True)
    owner=serializers.StringRelatedField()
