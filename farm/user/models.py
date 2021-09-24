from django.db import models

# Create your models here.
class MytreesInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=50, blank=True, null=True)
    set_time = models.DateTimeField(blank=True, null=True)
    get_time = models.DateTimeField(blank=True, null=True)
    orchard_id = models.IntegerField(blank=True, null=True)
    ut_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mytrees_info'


class Orchard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    advantage = models.CharField(max_length=100, blank=True, null=True)
    trees = models.CharField(max_length=100, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orchard'


class OrchardInfo(models.Model):
    id = models.AutoField(primary_key=True)
    info_address = models.CharField(max_length=100, blank=True, null=True)
    introduce = models.CharField(max_length=1000, blank=True, null=True)
    img_address = models.CharField(max_length=50, blank=True, null=True)
    img1 = models.CharField(max_length=50, blank=True, null=True)
    img2 = models.CharField(max_length=50, blank=True, null=True)
    img3 = models.CharField(max_length=50, blank=True, null=True)
    orchard_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orchard_info'


class OrchardTrees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    character = models.CharField(max_length=100, blank=True, null=True)
    season = models.CharField(max_length=2, blank=True, null=True)
    img = models.CharField(max_length=50, blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    bid = models.FloatField(blank=True, null=True)
    orchard_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orchard_trees'


class PovertyWork(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'poverty_work'


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    userimg = models.CharField(max_length=500, blank=True, null=True)
    wxid = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'


class UserTrees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_trees'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category'


class ComInfo(models.Model):
    id = models.AutoField(primary_key=True)
    commodity_id = models.IntegerField(blank=True, null=True)
    introduce = models.CharField(max_length=100, blank=True, null=True)
    img1 = models.CharField(max_length=100, blank=True, null=True)
    img2 = models.CharField(max_length=100, blank=True, null=True)
    img3 = models.CharField(max_length=100, blank=True, null=True)
    img4 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'com_info'


class Commodity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    orchar_id = models.IntegerField(blank=True, null=True)
    num_people = models.IntegerField(blank=True, null=True)
    bid = models.FloatField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'commodity'


class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    bid = models.FloatField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'shopping_cart'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=3, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order'


class OrderInfo(models.Model):
    order_id = models.CharField(primary_key=True, max_length=20)
    user_id = models.IntegerField(blank=True, null=True)
    commod_name = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    bid = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    buy_time = models.DateTimeField(blank=True, null=True)
    buy_method = models.CharField(max_length=4, blank=True, null=True)
    dispatching_method = models.CharField(max_length=4, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    require = models.CharField(max_length=100, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_info'


class CommodityInfo(models.Model):
    id = models.AutoField(primary_key=True)
    commodity_id = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    bid = models.FloatField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'commodity_info'


class CommodityWeight(models.Model):
    id = models.AutoField(primary_key=True)
    commodity_id = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'commodity_weight'


class Collect(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    commodity_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'collect'