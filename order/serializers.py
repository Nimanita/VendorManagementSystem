from rest_framework import serializers
from vendor.serializers import VendorSerializer
from vendor.models import Vendor
class VendorCodeField(serializers.RelatedField):
    def to_representation(self, value):
        return VendorSerializer(value).data
    
class PurchaseOrderSerializer(serializers.Serializer):
    
    purchase_order_code = serializers.UUIDField(read_only=True)
    order_date =  serializers.DateTimeField(allow_null = True)
    delivery_date = serializers.DateTimeField(allow_null = True)
    items = serializers.JSONField(default = {})
    quantity = serializers.IntegerField(default=0)
    status = serializers.CharField(default="pending")
    quality_rating = serializers.FloatField(default=0)
    issue_date = serializers.DateTimeField(allow_null = True)
    acknowledgment_date = serializers.DateTimeField(allow_null = True)
    
class PurchaseOrderDeserializer(serializers.Serializer):
    vendor_code = serializers.UUIDField(read_only=True)
    purchase_order_code = serializers.UUIDField(read_only=True)
    order_date =  serializers.DateTimeField(allow_null = True)
    delivery_date = serializers.DateTimeField(allow_null = True)
    items = serializers.JSONField(default = {})
    quantity = serializers.IntegerField(default=0)
    status = serializers.CharField(default="pending")
    quality_rating = serializers.FloatField(default=0)
    issue_date = serializers.DateTimeField(allow_null = True)
    acknowledgment_date = serializers.DateTimeField(allow_null = True)
