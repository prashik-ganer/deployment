from rest_framework import serializers
from .models import Orders, Contact, OrderUpdate, Product

class AllProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AllOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        # fields = ['order_id','seller','status']

# class AllProductsStockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SellerProductStock
#         fields = '__all__'