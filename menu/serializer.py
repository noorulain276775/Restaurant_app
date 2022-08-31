from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# Registration of Customer serializer

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Customer.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = "__all__"

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Customer.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


# serializer of User

class Userserializer(serializers.Serializer):

    class Meta:
        model = Customer
        fields = "__all__"


# Serializer for creating items

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


# Serializer for creating cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

# Serializer for creating Order


class OrderCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


# cart serializer with items to view the OrderItem in menu template

class CartItemSerializer(serializers.Serializer):
    item = ItemSerializer()
    class Meta:
        model= Cart
        fields= "__all__"

# Order view serializer with customer and item info to display on template

class OrderViewSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    order_item = CartItemSerializer()

    class Meta:
        model = Order
        fields = ("order_item", "customer", "created_at", "address", "status")

