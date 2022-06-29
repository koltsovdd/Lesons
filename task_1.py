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

DisplayData = Vendor.select(Vendor.vend_address, Customer.cust_name).where(Customer.cust_name == "Village Toys") \
        .join(Product) \
        .join(OrderItem)\
        .join(Order) \
        .join(Customer)\

for DisplayData in Vendor:
    print(f"{Vendor.vend_address} -->"
          f"{Customer.cust_name}")

    
