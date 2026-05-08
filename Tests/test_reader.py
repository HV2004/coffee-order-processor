import json 
import tempfile
from CsvReport.reader import Reader

def test_reader():
    sample = [
        {
            "order_id":"1",
            "drink":"latte",
            "size":"large",
            "price":5.5,
            "timestamp":"2026",
            "extras":["milk"]
        }
    ]
    with tempfile.NamedTemporaryFile(mode="w+",delete=False) as f:
        json.dump(sample,f)
        f.flush()
        reader = Reader()
        orders = reader.read(f.name)
    assert len(orders)==1
    assert orders[0].extras_count()==1
    