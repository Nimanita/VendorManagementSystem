from ..models import Vendor
from ..serializers import VendorSerializer
from django.http import HttpResponse
from rest_framework import status
import traceback

class VendorOperation:
    
    @classmethod
    def add_vendor(cls, data):
        try:
            
            vendor_data = VendorSerializer(data)
            Vendor.objects.create(**vendor_data.data)
            return HttpResponse("Vendor added successfully!" , status = status.HTTP_201_CREATED)
        
        except Exception as ex:
            print("exception" , ex)
            return HttpResponse("Operation failed" , status = status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def get_all_vendors(cls):
        try:
            vendors = Vendor.objects.all()
            all_vendors = VendorSerializer(vendors,many=True)
            return HttpResponse(all_vendors.data , status = status.HTTP_200_OK)    
        
        except Exception as ex:
            return HttpResponse("Operation failed" , status = status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def get_vendor(cls, vendor_code):
        try:
            print(type(vendor_code) , vendor_code)
            is_vendor_exist = cls.is_vendor_exist(vendor_code)
            if is_vendor_exist:
                vendors = Vendor.objects.filter(vendor_code = vendor_code)           
                vendor = VendorSerializer(vendors,many=True)
                return HttpResponse(vendor.data , status = status.HTTP_200_OK) 
            
        except Exception as ex:
            print(ex)
        return HttpResponse("Operation failed" , status = status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def update_vendor(cls, vendor_code , vendor_new_data):
        try:
            print("inside update" , vendor_code , vendor_new_data)
            is_vendor_exist = cls.is_vendor_exist(vendor_code)
            if is_vendor_exist:
                print("vendor_code" ,vendor_code ," dhdjd ", vendor_new_data )
                vendor_data = VendorSerializer(vendor_new_data)
                Vendor.objects.filter(vendor_code = vendor_code).update(**vendor_data.data)
                return HttpResponse("Vendor updated successfully!" , status = status.HTTP_200_OK)
        
        except Exception as ex:
            ex = traceback.format_exc()
            print("exception" , ex)
        return HttpResponse("Operation failed" , status = status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def delete_vendor(cls, vendor_code):
        try:
            is_vendor_exist = cls.is_vendor_exist(vendor_code)
            if is_vendor_exist:  
                Vendor.objects.filter(vendor_code = vendor_code).delete()
                return HttpResponse("Vendor deleted successfully!" , status = status.HTTP_200_OK)
       
        except Exception as ex:
            print(ex)
        return HttpResponse("Operation failed" , status = status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def is_vendor_exist(cls, vendor_code):
        try:
            
            is_exist = Vendor.objects.filter(vendor_code = vendor_code).exists()
            return is_exist
       
        except Exception as ex:
            print(ex)
            return False
    
    @classmethod
    def get_vendor_for_signal_operation(cls, vendor_code):
        try:
            is_vendor_exist = cls.is_vendor_exist(vendor_code)
            if is_vendor_exist:
                vendors = Vendor.objects.filter(vendor_code = vendor_code)           
                vendor = VendorSerializer(vendors,many=True)
                return vendor.data 
            
        except Exception as ex:
            print(ex)
        return None
