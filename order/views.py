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

from .services.PurchaseOrderOperation import PurchaseOrderOperation
# Create your views here

@api_view(['POST' , 'GET'])
def get_or_add_purchase_order(request):
   
    if request.method == 'POST' and request.data:
        return PurchaseOrderOperation.add_purchase_order(request.data)
    
    if request.method == 'GET':
        return PurchaseOrderOperation.get_all_purchase_orders()
  
    return HttpResponse("NOT FOUND" , status = status.HTTP_404_NOT_FOUND)
        
@api_view(['POST', 'GET' , 'DELETE'])
def get_or_update_purchase_order(request, purchase_order_code):
    print(request)
    if request.method == 'POST' and request.data:
        return PurchaseOrderOperation.update_purchase_order(purchase_order_code , request.data)
       
    if request.method == 'GET':
        return PurchaseOrderOperation.get_purchase_order(purchase_order_code)
    
    if request.method == 'DELETE':
        return PurchaseOrderOperation.delete_purchase_order(purchase_order_code)
    
    return HttpResponse("NOT FOUND" , status = status.HTTP_404_NOT_FOUND)

# Create your views here.
