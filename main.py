import argparse
import logging
from CsvReport.reader import Reader
from CsvReport.writer import Writer
from Tasks.service import Service
from Tasks.processor import Processor
from Tasks.validator import Valid
from Tasks.analytics import OrderAnalytics

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
    args = parser.parse_args()

    #Creating service layer
    OrderService = Service(
        reader=Reader(),
        writer=Writer(),
        validator=Valid(),
        processor=Processor()
    )

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
