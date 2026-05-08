from Tasks.validator import Valid
from Models.order import Order

validator = Valid()

# Test valid order
def test_valid_order():
    order = Order("1","latte","large",5.5,"2026",[])
    assert validator.validate(order)

# Test invalid order
def test_invalid_order():
    order = Order("2","tea","large",5.5,"2026",[])
    assert not validator.validate(order)

# Test invalid price
def test_invalid_price():
    order = Order("3","latte","large",-1,"2026",[])
    assert not validator.validate(order)

    