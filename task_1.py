from main import Vendor, Product, OrderItem, Order, Customer

# vendors = Vendor.select(Vendor.vend_id, Vendor.vend_name, Product.prod_id, OrderItem.quantity)\
#                 .join(Product)\
#                 .join(OrderItem)
#
# for vendor in vendors:
#     print(f"{vendor.vend_id} --> "
#           f"{vendor.vend_name} --> "
#           f"{vendor.product.prod_id} --> "
#           f"{vendor.product.orderitem.quantity}")

display_data = Vendor.select(Vendor.vend_address, OrderItem.order_id) \
        .join(Product) \
        .join(OrderItem)\
        .join(Order) \
        .join(Customer)\
        .where(Customer.cust_id == '1000000001') \

for data in display_data:
    print(f"{data.vend_address} -->"
          f"{data.product.orderitem.order_id}")

    
