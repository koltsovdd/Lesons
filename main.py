from peewee import *

from config import db


class BaseModel(Model):
    class Meta:
        database = db


class Customer(BaseModel):
    class Meta:
        db_table = "customers"

    cust_id = IntegerField()
    cust_name = TextField()
    cust_address = TextField()
    cust_state = TextField()
    cust_zip = TextField()
    cust_country = TextField()
    cust_contact = TextField()
    cust_email = TextField()
    cust_city = TextField()


class Vendor(BaseModel):
    class Meta:
        db_table = "vendors"

    vend_id = IntegerField(primary_key=True)
    vend_name = TextField(null=False)
    vend_address = TextField()
    vend_city = TextField()
    vend_state = TextField()
    vend_zip = TextField()
    vend_country = TextField()


class Product(BaseModel):
    class Meta:
        db_table = "products"

    prod_id = IntegerField(primary_key=True)
    vend_id = ForeignKeyField(Vendor)
    prod_name = TextField()
    prod_price = FloatField()
    prod_desc = TextField()


class Order(BaseModel):
    class Meta:
        db_table = "orders"

    order_num = IntegerField()
    order_date = TextField()
    cust_id = ForeignKeyField(Customer)


class OrderItem(BaseModel):
    class Meta:
        db_table = "orderitems"
        primary_key = CompositeKey('order_num', 'order_item')

    order_num = ForeignKeyField(Order)
    order_item = IntegerField()
    prod_id = ForeignKeyField(Product)
    quantity = IntegerField()
    item_price = FloatField()
