from Models.order import Order

# Test extras count
def test_extras_count():
    order = Order("1","latte","large",5.5,"2026",["milk","shot"])
    assert order.extras_count() == 2

# Test extras when None
def test_extras_empty():
    order = Order("2","latte","large",5.5,"2026",None)
    assert order.extras_count() == 0

# Test timestamp
def test_timestamp_format():
    order = Order("3","latte","large",5.5,None,[])
    assert order.timestamp_case() == "N/A"