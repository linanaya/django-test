from django.shortcuts import render
from django.http import *
import json,requests,jwt,datetime
from user.models import *
# Create your views here.

def shop_test(request):
    listuser = Commodity.objects.values()
    data = list(listuser)
    return HttpResponse(data)

def list_category(request):
    listuser = Category.objects.values()
    data = list(listuser)

    return JsonResponse({"data":data})

def process_commodity(request):
    request.params = request.GET
    id = request.params['id']
    com_data = Commodity.objects.values()
    com_data = list(com_data.filter(category_id=id))
    for i in com_data:
        orchard_data = Orchard.objects.values()
        orchard_data = list(orchard_data.filter(id=i['orchar_id']))
        i['orchard_id'] = orchard_data[0]["address"]+orchard_data[0]["name"]
    
    return JsonResponse({"data":com_data})

def commodity_info(request):
    request.params = request.GET
    id = request.params['id']
    com_info = ComInfo.objects.values()
    com_info = list(com_info.filter(commodity_id=id))
    com_data = Commodity.objects.values()
    com_data = list(com_data.filter(id=id))
    #添加字段
    orchard_data = Orchard.objects.values()
    orchard_data = list(orchard_data.filter(id=com_data[0]['orchar_id']))
    com_info[0]['bid'] = com_data[0]['bid']
    com_info[0]['name'] = com_data[0]['name']
    com_info[0]['address'] = orchard_data[0]['name']
    com_info[0]['orchard_id'] = com_data[0]['orchar_id']

    return JsonResponse({"data":com_info})

def process_commodity_info_detail1(request):
    request.params = request.GET
    commodity_id = request.params['id']
    commodity_info = CommodityInfo.objects.values()
    commodity_info = list(commodity_info.filter(commodity_id=commodity_id))

    return JsonResponse({"data":commodity_info})

def process_commodity_info_detail2(request):
    request.params = request.GET
    commodity_id = request.params['id']
    weight_list = CommodityWeight.objects.values()
    weight_list = list(weight_list.filter(commodity_id=commodity_id))

    return JsonResponse({"data":weight_list})

def process_shopcart(request):
    request.params = json.loads(request.body)
    token = request.params['token']
    data = jwt.decode(token, 'secret', issuer='farm', algorithms=['HS256'])
    user_id = data['data']['user_id']
    name = request.params['name']
    bid = request.params['bid']
    number = request.params['number']
    weight = request.params['weight']
    img = request.params['img']
    cart = ShoppingCart.objects.create(
        user_id=user_id,
        name=name,
        bid=bid,
        number=number,
        weight=weight,
        img=img
    )

    return JsonResponse({"data":"OK"})

def cart_list(request):
    request.params = request.GET
    token = request.params['token']
    data = jwt.decode(token, 'secret', issuer='farm', algorithms=['HS256'])
    id = data['data']['user_id']
    cart = ShoppingCart.objects.values()
    cart = list(cart.filter(user_id=id))

    return JsonResponse({"data":cart})


def process_order(request):
    request.params = request.GET
    token = request.params['token']
    data = jwt.decode(token, 'secret', issuer='farm', algorithms=['HS256'])
    id = data['data']['user_id']
    user = User.objects.values()
    user = list(user.filter(id=id))
    data=[]
    data.append(user[0]['username'])
    data.append(user[0]['tel'])
    data.append(user[0]['address'])
    data.append("普通快递")

    return JsonResponse({"data":data})