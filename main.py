import argparse
from CsvReport.reader import Reader
from CsvReport.writer import Writer
from Tasks.service import Service
from Tasks.processor import Processor
from Tasks.validator import Valid

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    OrderService = Service(
        reader=Reader(),
        writer=Writer(),
        validator=Valid(),
        processor=Processor()
    )
    OrderService.execute(args.input,args.output)
