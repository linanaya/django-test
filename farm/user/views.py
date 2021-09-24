from django.shortcuts import render
from django.http import *
import json,requests,jwt,datetime
from .models import *
# Create your views here.

def test(request):
    listuser = User.objects.values()
    data = list(listuser)
    return HttpResponse(data)

def login(request):
    request.params = request.GET
    print(request.params['code'])
    date = {
        'appid': 'wx0c4879a0dbdbc922',
        'secret': '6c99d04f49add4c1d31131d97b147051',
        'js_code': request.params['code'],
        'grant_type': 'authorization_code'
    }
    response = requests.get('https://api.weixin.qq.com/sns/jscode2session', params=date)
    print(response.text)
    openid = response.json()['openid']
    user = User.objects.values()
    user = list(user.filter(wxid=openid))
    id = 0
    if_new = False
    if len(user) == 0:
        user_data = User.objects.create(
            wxid=openid
        )
        id = user_data.id
        if_new = True
    else:
        id = user[0]['id']

    # 对用户id使用jwt加密
    dic = {
        'exp': datetime.datetime.now() + datetime.timedelta(days=1),  # 过期时间
        'iat': datetime.datetime.now(),  # 开始时间
        'iss': 'farm',  # 签名
        'data': {  # 内容，一般存放该用户id和开始时间
            'user_id': id,
        },
    }
    token = jwt.encode(dic, 'secret', algorithm='HS256')  # 加密生成字符串

    return JsonResponse({"token": token, "if_new": if_new})

def access_userinfo(request):
    request.params = json.loads(request.body)
    token = request.params['token']
    userimg = request.params['userimg']
    username = request.params['username']
    data = jwt.decode(token, 'secret', issuer='farm', algorithms=['HS256'])
    id = data['data']['user_id']
    user = User.objects.get(id=id)
    user.username = username
    user.userimg = userimg
    user.save()

    return JsonResponse({"data":"OK!"})

def access_usertrees(request):
    request.params = request.GET
    token = request.params['token']
    data = jwt.decode(token, 'secret', issuer='farm', algorithms=['HS256'])
    id = data['data']['user_id']
    usertrees = UserTrees.objects.values()
    usertrees = list(usertrees.filter(user_id=id))

    return JsonResponse({"data":usertrees})

def access_utclassify(request):
    request.params = request.GET
    ut_id = request.params['ut_id']
    usertrees_info = MytreesInfo.objects.values()
    usertrees_info = list(usertrees_info.filter(ut_id=ut_id))
    orchard = Orchard.objects.values()

    #用for循环把usertrees_info 里面的orchard_id信息替换成具体信息
    for data in usertrees_info:
        info = []
        orchard_info = list(orchard.filter(id=data['orchard_id']))
        info.append(orchard_info[0]['name'])
        info.append(orchard_info[0]['address'])
        data['orchard_id'] = info
    
    return JsonResponse({"data":usertrees_info})

def process_main(request):
    request.params = json.loads(request.body)
    address = request.params['address']
    tel = request.params['tel']
    token = request.params['token']
    data = jwt.decode(token, 'secret', issuer='farm', algorithms=['HS256'])
    id = data['data']['user_id']
    user = User.objects.get(id=id)
    user.tel = tel
    user.address = address
    user.save()

    return JsonResponse({"data":"OK"})

def process_collect(request):
    request.params = request.GET
    token = request.params['token']
    data = jwt.decode(token, 'secret', issuer='farm', algorithms=['HS256'])
    id = data['data']['user_id']
    commodity_id = request.params['commodity_id']
    collect = Collect.objects.create(
        user_id=id,
        commodity_id=commodity_id
    )

    return JsonResponse({"data":"OK"})

def collect_list(request):
    request.params = request.GET
    token = request.params['token']
    data = jwt.decode(token, 'secret', issuer='farm', algorithms=['HS256'])
    id = data['data']['user_id']
    commodity_ids = Collect.objects.values()
    commodity_ids = list(commodity_ids.filter(user_id=id))
    data = []
    for i in commodity_ids:
        commodity = Commodity.objects.values()
        commodity = list(commodity.filter(id=i['commodity_id']))
        data.append(commodity[0])

    return JsonResponse({"data":data})

def del_cart(request):
    request.params = json.loads(request.body)
    ids = request.params['ids']
    for i in ids:
        cart = ShoppingCart.objects.get(id=i)
        cart.delete()

    return JsonResponse({"data":"OK"})