from .models import *
from rest_framework import serializers

class demo_serializer(serializers.Serializer):
        p_id=serializers.IntegerField(read_only=True)
        product_name = serializers.CharField()
        product_price = serializers.IntegerField()

        def create(self, validated_data):
            return Product.objects.create(**validated_data)
        def update(self, instance, validated_data):   
            instance.product_name = validated_data.get('product_name', instance.product_name)
            instance.product_price = validated_data.get('product_price', instance.product_price)
            instance.save()
            return instance
