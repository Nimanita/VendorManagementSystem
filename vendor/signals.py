from django.dispatch import receiver
from order.signals import order_created , order_update
from vendor.services.VendorOperation import VendorOperation
import json
from .serializers import VendorSerializer 
from django.core.serializers import serialize
from datetime import datetime , timedelta
import traceback


@receiver(order_created)
def update_quantity_on_new_order(sender, **kwargs):
   
    vendor_obj = VendorSerializer(sender.vendor_code)
    vendor = vendor_obj.data
    fulfilled_order = vendor["total_purchase_order"] * vendor["fulfillment_rate"]
    fulfilled_order = round(fulfilled_order)
    vendor["total_purchase_order"] = vendor["total_purchase_order"] + 1
    vendor["fulfillment_rate"] = fulfilled_order/vendor["total_purchase_order"]
    VendorOperation.update_vendor(vendor["vendor_code"],vendor)

@receiver(order_update)
def update_quantity_on_order(sender, purchase_order, vendor_obj, **kwargs):
   
    try :
        purchase_order_obj = purchase_order[0]
        vendor = serialize('json', [vendor_obj])
        vendor_in_json = json.loads(vendor)
       
        vendors = VendorOperation.get_vendor_for_signal_operation(vendor_in_json[0]["pk"])
        vendor = vendors[0]
        
        #quality_rating_calculation
        prev_quality_rate = vendor["quality_rating_avg"]*vendor["completed_purchase_order"]
        new_quality_rate = purchase_order_obj["quality_rating"] + prev_quality_rate
        
        #on_time_delivery_rate_calculation
        prev_fulfilled_order = vendor["total_purchase_order"] * vendor["fulfillment_rate"]
        prev_fulfilled_order = round(prev_fulfilled_order)
        
        #response_time_calculation
        prev_response_time = vendor["average_response_time"] * vendor["completed_purchase_order"]
        issue_date = datetime.strptime(purchase_order_obj["issue_date"], "%Y-%m-%dT%H:%M:%S.%fZ")
        acknowledgment_date = datetime.strptime(purchase_order_obj["acknowledgment_date"], "%Y-%m-%dT%H:%M:%S.%fZ")
        prev_response_time_in_second = timedelta(seconds = prev_response_time)
        new_response_time_obj = issue_date - acknowledgment_date + prev_response_time_in_second
        new_response_time = new_response_time_obj.total_seconds()
        
        if(purchase_order_obj["delivery_date"] <= purchase_order_obj["issue_date"]):
            vendor["on_time_completed_purchase_order"] = vendor["on_time_completed_purchase_order"] + 1
        
        vendor["completed_purchase_order"] = vendor["completed_purchase_order"] + 1
        vendor["fulfillment_rate"] = vendor["on_time_completed_purchase_order"]/vendor["completed_purchase_order"]
        vendor["quality_rating_avg"] = new_quality_rate/vendor["completed_purchase_order"]
        vendor["average_response_time"] = new_response_time/vendor["completed_purchase_order"]

        VendorOperation.update_vendor(vendor["vendor_code"],vendor)
    except Exception as ex:
        expt = traceback.format_exc()
        print("exception" , expt)


