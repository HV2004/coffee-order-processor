import json
from Models.order import Order
class Reader:
    def read(self,file_path):
        with open(file_path,"r") as f:
            data = json.load(f)
        orders = []
        for i in data:
            order = Order(
                order_id = i.get("order_id"),
                drink = i.get("drink"),
                size = i.get("size"),
                price = i.get("price"),
                timestamp = i.get("timestamp"),
                extras = i.get("extras")
            )
            orders.append(order)
        return orders
    
