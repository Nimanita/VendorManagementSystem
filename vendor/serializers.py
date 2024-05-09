from rest_framework import serializers



class VendorSerializer(serializers.Serializer):

    vendor_code = serializers.UUIDField(read_only=True)
    name= serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=200)
    contact_num = serializers.IntegerField(default=1234567890)
    on_time_delivery_rate = serializers.FloatField(default=0) 
    quality_rating_avg = serializers.FloatField(default=0)
    average_response_time = serializers.FloatField(default=0)
    fulfillment_rate = serializers.FloatField(default=0)
    total_purchase_order = serializers.IntegerField(default=0)
    completed_purchase_order = serializers.IntegerField(default=0)
    on_time_completed_purchase_order = serializers.IntegerField(default=0)


