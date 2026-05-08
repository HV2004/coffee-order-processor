import logging

logger = logging.getLogger(__name__)

class Service:
    """
    Coordinates the entire ordering process
    """

    def __init__(self,reader,writer,validator,processor):
        self.reader = reader
        self.writer = writer
        self.validator = validator
        self.processor = processor

    def execute(self,input_file,output_file):
        """
        Executes the order workflow
        """

        logger.info(f"Starting order processing workflow")

        orders = self.reader.read(input_file) #Reads orders workflow
        processed_rows = []
        valid_orders = []

        for o in orders:

            #skips invalid orders
            if not self.validator.validate(o):
                logger.warning(f"Skipping Invalid order: {o.order_id}")
                continue
            valid_orders.append(o)
            processed = self.processor.process(o) # Process valid order
            processed_rows.append(processed)

        self.writer.write(output_file,processed_rows) # Write final CSV report 

        logger.info(f"Total valid orders processed: {len(valid_orders)}")
        
        return valid_orders

