from Tasks.processor import Processor
from Models.order import Order

# Test processor output
def test_process():
    processor = Processor()
    order = Order("ORD-1","latte","large",5.5,None,["milk"])
    result = processor.process(order)
    assert result == ["ORD-1","latte","large","5.50","N/A",1]
    