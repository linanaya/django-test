import requests,jwt,datetime
# data={
#     "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mjc0NjkwNzEsImlhdCI6MTYyNzM4MjY3MSwiaXNzIjoiZmFybSIsImRhdGEiOnsidXNlcl9pZCI6Mn19.Hyzan0JbhjrQUfQbvvyJAcNVkwHVN7UDxqkMTcznuF0",
#     "name":"测试",
#     "bid":10.5,
#     "number":2,
#     "weight":5,
#     "total":21,
#     "dispatching_method":"普通快递",
#     "address":"江苏淮安丽江公园32栋",
#     "require":"不要给我压坏了",
#     "img":"test.png"
# }
data = {
    "ids":[3]
    #"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mjc0NjkwNzEsImlhdCI6MTYyNzM4MjY3MSwiaXNzIjoiZmFybSIsImRhdGEiOnsidXNlcl9pZCI6Mn19.Hyzan0JbhjrQUfQbvvyJAcNVkwHVN7UDxqkMTcznuF0"
}
response = requests.post("http://127.0.0.1/user/cart/del",json=data)
print(response.status_code)
print(response.json())
# dic = {
#     'exp': datetime.datetime.now() + datetime.timedelta(days=1),  # 过期时间
#     'iat': datetime.datetime.now(),  #  开始时间
#     'iss': 'farm',  # 签名
#     'data': {  # 内容，一般存放该用户id和开始时间
#         'user_id':2,
#             },
#     }
# token = jwt.encode(dic, 'secret', algorithm='HS256')  # 加密生成字符串
# print(token)