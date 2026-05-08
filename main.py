import argparse
from CsvReport.reader import Reader
from CsvReport.writer import Writer
from Tasks.service import Service
from Tasks.processor import Processor
from Tasks.validator import Valid
from Tasks.analytics import OrderAnalytics

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--summary",required=False)
    args = parser.parse_args()
    OrderService = Service(
        reader=Reader(),
        writer=Writer(),
        validator=Valid(),
        processor=Processor()
    )
    valid_orders = OrderService.execute(args.input,args.output)
    if args.summary:
        analytics = OrderAnalytics()
        analytics.generate_summary(valid_orders,args.summary)
        

if __name__=="__main__":
    main()
