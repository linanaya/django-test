from django.shortcuts import render
from django.http import *
import json,requests,jwt,datetime
from user.models import *

# Create your views here.
def process_orchardinfo(request):
    orchard_info = Orchard.objects.values()
    orchard_info = list(orchard_info)

    return JsonResponse({"data":orchard_info})

def process_orchardintroduce(request):
    request.params = request.GET
    orchard_id = request.params['id']
    data = OrchardInfo.objects.values()
    data = list(data.filter(orchard_id=orchard_id))

    return JsonResponse({"data":data})

def process_orchardstore(request):
    request.params = request.GET
    orchard_id = request.params['id']
    store_info = OrchardTrees.objects.values()
    store_info = list(store_info.filter(orchard_id=orchard_id))

    return JsonResponse({"data":store_info})

def poverty_list(request):
    data = PovertyWork.objects.values()
    data = list(data)

    return JsonResponse({"data":data})