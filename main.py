import argparse
import logging
from CsvReport.reader import Reader
from CsvReport.writer import Writer
from Tasks.service import Service
from Tasks.processor import Processor
from Tasks.validator import Valid
from Tasks.analytics import OrderAnalytics
from Data.data_exchange import DataStorage
from API.exchange_rate_api import ExchangeRateApi

#Configure logging
logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    """
    Entry point of the System.
    Handles arguement  parsing and coordinates application flow.
    """
    logger.info("Application started")
    parser = argparse.ArgumentParser() # Create CLI parser
    parser.add_argument("--input",required=True) # Input JSON file
    parser.add_argument("--output", required=True) # Output CSV file
    parser.add_argument("--summary",required=False) # Analytics summary file
    parser.add_argument("--currency",required=False) # Currency conversion 
    args = parser.parse_args()
    data_exchange = DataStorage()

    #Creating service layer
    OrderService = Service(
        reader=Reader(),
        writer=Writer(),
        validator=Valid(),
        processor=Processor(),
        data_exchange = data_exchange
    )


    #Converts the currency
    currency = args.currency if args.currency else "USD"
    data_exchange.set_currency(currency)
    rate = 1
    if currency!="USD":
        rate = ExchangeRateApi.get_exchange_rate(currency)
        data_exchange.set_exchange_rate(rate)

    if rate is None:
        logger.error("ERROR Failed to fetch exchange rate")
        print("Failed to fetch exchange rate")
        exit(1)

    # Execute processing workflow
    valid_orders = OrderService.execute(args.input,args.output)

    logger.info("CSV report generated successfully")

    #Generate analytics summary if requested
    if args.summary:

        logger.info("Generating analytics summary")
        analytics = OrderAnalytics()
        analytics.generate_summary(valid_orders,args.summary)

        logger.info("Summary report generated successfully")
        logger.info("Application finished") 
    

if __name__=="__main__":
    main()
