from ..models import PurchaseOrder
from ..serializers import PurchaseOrderSerializer , PurchaseOrderDeserializer
from django.http import HttpResponse
from rest_framework import status
from django.dispatch import receiver
from order.signals import order_created , order_update
from vendor.models import Vendor
import datetime
from django.core import serializers
import traceback
class PurchaseOrderOperation:
    
    @classmethod
    def add_purchase_order(cls, data):
        try:
            
            data["order_date"] = datetime.datetime.now()
            purchase_order_data = PurchaseOrderSerializer(data)
            vendor_obj = Vendor.objects.get(vendor_code = data["vendor_code"])
            purchase_order_obj = PurchaseOrder.objects.create(**purchase_order_data.data , vendor_code= vendor_obj )
            order_created.send(sender=purchase_order_obj)
            return HttpResponse("PurchaseOrder added successfully!" , status = status.HTTP_201_CREATED)
        
        except Exception as ex:
            expt = traceback.format_exc()
            print("exception" , expt)
            return HttpResponse("Operation failed" , status = status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def get_all_purchase_orders(cls):
        try:
            purchase_orders = PurchaseOrder.objects.all()
            
            all_purchase_orders = PurchaseOrderDeserializer(purchase_orders,many=True)
            print("all_purchase_orders" , all_purchase_orders.data)
            return HttpResponse(all_purchase_orders.data , status = status.HTTP_200_OK)    
        
        except Exception as ex:
            expt = traceback.format_exc()
            print("exception" , expt)
            return HttpResponse("Operation failed" , status = status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def get_purchase_order(cls, purchase_order_code):
        try:
            is_purchase_order_exist = cls.is_purchase_order_exist(purchase_order_code)
            if is_purchase_order_exist:
                purchase_orders = PurchaseOrder.objects.filter(purchase_order_code = purchase_order_code)           
                purchase_order = PurchaseOrderDeserializer(purchase_orders,many=True)
                return HttpResponse(purchase_order.data , status = status.HTTP_200_OK) 
            
        except Exception as ex:
            expt = traceback.format_exc()
            print("exception" , expt)
        return HttpResponse("Operation failed" , status = status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def update_purchase_order(cls, purchase_order_code , purchase_order_new_data):
        try:
            is_purchase_order_exist = cls.is_purchase_order_exist(purchase_order_code)
            if is_purchase_order_exist:
                
                purchase_order_data = PurchaseOrderSerializer(purchase_order_new_data)
                vendor_obj = Vendor.objects.get(vendor_code = purchase_order_new_data["vendor_code"])
                result = PurchaseOrder.objects.filter(purchase_order_code = purchase_order_code).update(**purchase_order_data.data , vendor_code = vendor_obj)
                
                if(purchase_order_new_data["status"] == "completed" and result == 1):
                    purchase_orders = PurchaseOrder.objects.filter(purchase_order_code = purchase_order_code)           
                    purchase_order = PurchaseOrderDeserializer(purchase_orders,many=True)
                    print(purchase_order.data)
                    order_update.send(sender=cls, purchase_order = purchase_order.data, vendor_obj = vendor_obj )
                
                return HttpResponse("PurchaseOrder updated successfully!" , status = status.HTTP_200_OK)
        
        except Exception as ex:
            expt = traceback.format_exc()
            print("exception" , expt)
        return HttpResponse("Operation failed" , status = status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def delete_purchase_order(cls, purchase_order_code):
        try:
            is_purchase_order_exist = cls.is_purchase_order_exist(purchase_order_code)
            if is_purchase_order_exist:  
                PurchaseOrder.objects.filter(purchase_order_code = purchase_order_code).delete()
                return HttpResponse("PurchaseOrder deleted successfully!" , status = status.HTTP_200_OK)
       
        except Exception as ex:
            expt = traceback.format_exc()
            print("exception" , expt)
        return HttpResponse("Operation failed" , status = status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def is_purchase_order_exist(cls, purchase_order_code):
        try:
            
            is_exist = PurchaseOrder.objects.filter(purchase_order_code = purchase_order_code).exists()
            return is_exist
       
        except Exception as ex:
            expt = traceback.format_exc()
            print("exception" , expt)
            return False
        