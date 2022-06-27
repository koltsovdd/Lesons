from peewee import *

db = PostgresqlDatabase('', user='postgres', password='',
                        host='127.0.0.1', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


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


class OrderItem(BaseModel):
    class Meta:
        db_table = "orderitems"
        primary_key = CompositeKey('order_num', 'order_item')

    order_num = ForeignKeyField(Orders)
    order_item = IntegerField()
    prod_id = ForeignKeyField(Product)
    quantity = IntegerField()
    item_price = FloatField()


vendors = Vendor.select(Vendor.vend_id, Vendor.vend_name, Product.prod_id, OrderItem.quantity)\
                .join(Product)\
                .join(OrderItem)

for vendor in vendors:
    print(f"{vendor.vend_id} --> "
          f"{vendor.vend_name} --> "
          f"{vendor.product.prod_id} --> "
          f"{vendor.product.orderitem.quantity}")





