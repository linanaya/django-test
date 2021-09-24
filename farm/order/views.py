from django.shortcuts import render
from django.http import *
import json,requests,jwt,datetime,random
from user.models import *
# Create your views here.

def order_test(request):
    listuser = OrderInfo.objects.values()
    data = list(listuser)
    return HttpResponse(data)

def order_complete(request):
    request.params = json.loads(request.body)
    token = request.params['token']
    data = jwt.decode(token, 'secret', issuer='farm', algorithms=['HS256'])
    id = data['data']['user_id']
    name = request.params['name']
    bid = request.params['bid']
    number = request.params['number']
    total = request.params['total']
    weight = request.params['weight']
    dispatching_method = request.params['dispatching_method']
    address = request.params['address']
    require = request.params['require']
    img = request.params['img']
    order_id = ''
    for i in range(8):
        order_id += str(random.randint(0,9))
    t = datetime.datetime.now()
    order_info = OrderInfo.objects.create(
        order_id=order_id,
        user_id=id,
        commod_name=name,
        number=number,
        bid=bid,
        total=total,
        weight=weight,
        buy_time=t,
        buy_method="微信支付",
        dispatching_method=dispatching_method,
        address=address,
        require=require,
        img=img
    )
    order = Order.objects.create(
        time=t,
        status="已收货",
        order_id=order_id,
        user_id=id
    )

    return JsonResponse({"data":order_info.id})

def order_list(request):
    request.params = request.GET
    token = request.params['token']
    data = jwt.decode(token, 'secret', issuer='farm', algorithms=['HS256'])
    id = data['data']['user_id']
    order = Order.objects.values()
    order = list(order.filter(user_id=id))
    for i in order:
        order_info = OrderInfo.objects.values()
        order_info = list(order_info.filter(order_id=i['order_id']))
        del order_info[0]['weight']
        del order_info[0]['buy_time']
        del order_info[0]['buy_method']
        del order_info[0]['dispatching_method']
        del order_info[0]['require']
        i['order_id'] = order_info[0]

    return JsonResponse({"data":order})

def order_info(request):
    request.params = request.GET
    order_id = request.params['id']
    info = OrderInfo.objects.values()
    info = list(info.filter(order_id=order_id))

    return JsonResponse({"data":info})
