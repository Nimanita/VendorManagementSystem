from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import  render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import random
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json 
from rest_framework.parsers import JSONParser
from .services.VendorOperation import VendorOperation

# Create your views here.

@api_view(['POST' , 'GET'])
def get_or_add_vendor(request):
   
    if request.method == 'POST' and request.data:
        return VendorOperation.add_vendor(request.data)
    
    if request.method == 'GET':
        return VendorOperation.get_all_vendors()
  
    return HttpResponse("NOT FOUND" , status = status.HTTP_404_NOT_FOUND)
        
@api_view(['POST', 'GET' , 'DELETE'])
def get_or_update_vendor(request, vendor_code):
    print(request)
    if request.method == 'POST' and request.data:
        return VendorOperation.update_vendor(vendor_code , request.data)
       
    if request.method == 'GET':
        return VendorOperation.get_vendor(vendor_code)
    
    if request.method == 'DELETE':
        return VendorOperation.delete_vendor(vendor_code)
    
    return HttpResponse("NOT FOUND" , status = status.HTTP_404_NOT_FOUND)

