from Data.data_exchange import DataStorage

def test_orders_stortage():
    data = DataStorage()
    orders = [{"drink":"latte"}]
    data.set_orders(orders)
    assert data.get_orders() == orders

def test_currency():
    data = DataStorage()
    data.set_currency("EUR")
    assert data.get_currency() == "EUR"