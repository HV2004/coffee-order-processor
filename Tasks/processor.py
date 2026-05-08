import logging
logger = logging.getLogger(__name__)

class Processor:
    """
    Processes valid orders into CSV format
    """

    def process(self,order):
        """
        Converts order object into output row.
        """

        logger.info(f"Processing order: {order.order_id}")

        processed_row = [order.order_id,order.drink,order.size,f"{order.price:.2f}",order.timestamp_case(),order.extras_count()]
        
        logger.info(f"Order processed successfully: {order.order_id}")

        return processed_row