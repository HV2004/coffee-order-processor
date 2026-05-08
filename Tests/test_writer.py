import tempfile
import csv
from CsvReport.writer import Writer

def test_writer():
    rows = [["1","latte","large","5.50","2026",1]]

    with tempfile.NamedTemporaryFile(mode="r+",newline="",delete=False) as f:
        writer = Writer()
        writer.write(f.name,rows)
        f.seek(0)
        data = list(csv.reader(f))

    assert data[1] == ["1","latte","large","5.50","2026","1"]

    
