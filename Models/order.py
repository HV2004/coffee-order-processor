import logging

logger = logging.getLogger(__name__)

class Order:

    #Represents a single coffee order
    def __init__(self,order_id,drink,size,price,timestamp,extras):
        self.order_id = order_id
        self.drink = drink
        self.size = size
        self.price = price
        self.timestamp = timestamp
        self.extras = extras
    
        logger.info(f"Order object created: {self.order_id}")

    def extras_count(self):
        #Returns the number of extras
        count = len(self.extras)
        if self.extras:
            logger.info(f"Extras count calculated for {self.order_id}:{count}")
            return count
        else:
            logger.info(f"Extras count calculated for {self.order_id}: 0")
            return 0
    
    def timestamp_case(self):
        """"
        Returns formatted timestamp.
        If timestamp is missing, returns N/A.
        """
        if self.timestamp:
            return self.timestamp
        
        logger.warning(f"Missing timestamp for order: {self.order_id}")
        return "N/A"
        
    