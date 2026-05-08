from Tasks.analytics import OrderAnalytics
from Models.order import Order

def test_analytics():
    analytics = OrderAnalytics()
    orders = [
        Order("1","latte","large",5.0,None,[]),
        Order("2","espresso","small",3.0,None,[]),
    ]

    analytics.generate_summary(orders,"test_summary.json")

    import json
    with open("test_summary.json") as f:
        data = json.load(f)
    assert data["total_orders"] == 2
    assert data["total_revenue"] == 8.0
    