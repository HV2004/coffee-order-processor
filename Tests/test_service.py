from Tasks.service import Service

class MockReader:
    def read(self,_):
        return ["valid","invalid"]
    
class MockValidator:
    def validate(self,order):
        return order == "valid"

class MockProcesstor:
    def process(self,order):
        return [order]
    
class MockWriter:
    def __init__(self):
        self.output = None

    def write(self,_,rows):
        self.output= rows

def test_service_flow():
    writer = MockWriter()
    service = Service(
        reader=MockReader(),
        writer=writer,
        validator=MockValidator(),
        processor=MockProcesstor()
    )
    service.execute("input.json","output.csv")

    assert writer.output == [["valid"]]