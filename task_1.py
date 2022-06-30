from peewee import fn

from main import Vendor, Product, OrderItem, Order, Customer, User, Message

# vendors = Vendor.select(Vendor.vend_id, Vendor.vend_name, Product.prod_id, OrderItem.quantity)\
#                 .join(Product)\
#                 .join(OrderItem)
#
# for vendor in vendors:
#     print(f"{vendor.vend_id} --> "
#           f"{vendor.vend_name} --> "
#           f"{vendor.product.prod_id} --> "
#           f"{vendor.product.orderitem.quantity}")

# display_data = Vendor.select(Vendor.vend_address, OrderItem.order_id) \
#         .join(Product) \
#         .join(OrderItem)\
#         .join(Order) \
#         .join(Customer)\
#         .where(Customer.cust_id == '1000000001') \
#
# for data in display_data:
#     print(f"{data.vend_address} -->"
#           f"{data.product.orderItem.order_id}")


display_users = User.select(User.user_id, User.user_age, User.user_name, User.user_email, User.user_surname)

display_messages = Message.select(Message.message_id, Message.message_text, Message.from_user_id, Message.to_user_id)

display_user_1 = Message.select(Message.message_text)\
            .where(Message.to_user_id == 1, Message.to_user_id == 1)

display_some_information = User.select(User.user_name, Message.message_text)\
            .join(Message, on=User.user_id == Message.to_user_id)\
            .where(Message.from_user_id == 1, Message.to_user_id == 1)

display_surnames_and_count_2 = User.select(User.user_surname, fn.count(Message.to_user_id))\
            .join(Message, on=User.user_id == Message.to_user_id)\
            .group_by(Message.to_user_id)

display_surnames_and_count_2 = User.select(User.user_surname, fn.count(Message.from_user_id))\
            .join(Message, on=User.user_id == Message.from_user_id)\
            .group_by(Message.from_user_id)


display_users_avg_age = User.select(fn.avg(User.user_age))




