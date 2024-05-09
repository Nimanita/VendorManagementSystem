from django.db import models
import uuid
from datetime import datetime
# Create your models here.
class Vendor(models.Model): 
    vendor_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False , db_index=True)
    name= models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_num = models.IntegerField(default=1234567890)
    on_time_delivery_rate = models.FloatField(default=0) 
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)
    total_purchase_order = models.IntegerField(default=0)
    completed_purchase_order = models.IntegerField(default=0)
    on_time_completed_purchase_order = models.IntegerField(default=0)
    