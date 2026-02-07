from rest_framework import serializers
from .models import Client, Product, Employee, Sale

# ----------------------
# Client Serializer
# ----------------------
class ClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=70)
    age = serializers.IntegerField(min_value=18, max_value=100)

    class Meta:
        model = Client
        fields = ['id', 'name', 'age', 'created_at']


# ----------------------
# Product Serializer
# ----------------------
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'description', 'quantity']


# ----------------------
# Employee Serializer
# ----------------------
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'registration']


# ----------------------
# Sale Serializer
# ----------------------
class SaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), source='client', write_only=True
    )

    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='employee', write_only=True
    )

    class Meta:
        model = Sale
        fields = [
            'id',
            'product', 'product_id',
            'client', 'client_id',
            'employee', 'employee_id',
            'nrf'
        ]
