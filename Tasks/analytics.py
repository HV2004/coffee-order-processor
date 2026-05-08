import json
from collections import Counter

class OrderAnalytics:
    def generate_summary(self,orders,summary_file):
        total_orders = len(orders)
        total_revenue = sum(order.price for order in orders)
        avg_order_value = (total_revenue/total_orders if total_orders>0 else 0)
        drink_counter = Counter(order.drink for order in orders)
        size_counter = Counter(order.size for order in orders)
        summary = {
            "total_orders":total_orders,
            "total_revenue":round(total_revenue,2),
            "average_order_value":round(avg_order_value,2),
            "order_by_drink":dict(drink_counter),
            "order_by_size":dict(size_counter)
        }
        with open(summary_file,"w") as f:
            json.dump(summary,f,indent=4)
