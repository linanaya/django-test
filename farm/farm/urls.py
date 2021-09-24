"""farm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings
from user.views import *
from orchard.views import *
from shop.views import *
from order.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/test',test),
    path('user/login',login),
    path('user/info',access_userinfo),
    path('user/trees',access_usertrees),
    path('user/trees/classify',access_utclassify),
    path('orchard/info',process_orchardinfo),
    path('orchard/introduce',process_orchardintroduce),
    path('orchard/store',process_orchardstore),
    path('poverty/work',poverty_list),
    path('shop/test',shop_test),
    path('shop/category',list_category),
    path('shop/commodity',process_commodity),
    path('shop/commodity/info',commodity_info),
    path('order/test',order_test),
    path('user/main',process_main),
    path('shop/commodity/info/detail1',process_commodity_info_detail1),
    path('shop/commodity/info/detail2',process_commodity_info_detail2),
    path('shop/cart',process_shopcart),
    path('user/cart',cart_list),
    path('user/collect',process_collect),
    path('shop/commodity/order',process_order),
    path('order/complete',order_complete),
    path('order/list',order_list),
    path('order/info',order_info),
    path('user/collect/list',collect_list),
    path('user/cart/del',del_cart),
    
]
urlpatterns += static('images/', document_root=settings.STATIC_ROOT)
