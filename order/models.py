from django.db import models
import uuid
from datetime import datetime
from django.utils import timezone
from vendor.models import Vendor
# Create your models here.
class PurchaseOrder(models.Model): 
    purchase_order_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_code = models.ForeignKey(Vendor , on_delete = models.CASCADE) 
    order_date = models.DateTimeField(null = False , default="0")
    delivery_date = models.DateTimeField(null = False)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20 , default="pending")
    quality_rating = models.FloatField(default=0)
    issue_date = models.DateTimeField(null = True)
    acknowledgment_date = models.DateTimeField(null = True)