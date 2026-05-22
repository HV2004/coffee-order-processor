import logging

logger = logging.getLogger(__name__)

class Service:
    """
    Coordinates the entire ordering process
    """

    def __init__(self,reader,writer,validator,processor,data_exchange):
        self.reader = reader
        self.writer = writer
        self.validator = validator
        self.processor = processor
        self.data_exchange = data_exchange

    def execute(self,input_file,output_file):
        """
        Executes the order workflow
        """

        logger.info(f"Starting order processing workflow")

        orders = self.reader.read(input_file) #Reads orders workflow
        self.data_exchange.set_orders(orders)
        processed_rows = []
        valid_orders = []

        for o in self.data_exchange.get_orders():

            #skips invalid orders
            if not self.validator.validate(o):
                logger.warning(f"Skipping Invalid order: {o.order_id}")
                continue
            valid_orders.append(o)
            processed = self.processor.process(o,self.data_exchange.get_exchange_rate(),self.data_exchange.get_currency()) # Process valid order
            processed_rows.append(processed)
            
        self.data_exchange.set_processed_orders(valid_orders)
        self.writer.write(output_file,processed_rows) # Write final CSV report 

        logger.info(f"Total valid orders processed: {len(valid_orders)}")
        
        return valid_orders

