import logging

logger = logging.getLogger(__name__)
class Valid:
    """
    Validates coffee orders
    """

    drinks = {"espresso","latte","cappuccino","americano"}
    sizes = {"small","medium","large"}

    def validate(self, order):
        """
        Validates order fileds.
        """

        #Validate drink
        if order.drink not in self.drinks:
            logger.warning(f"Invalid drink detected: {order.drink}")
            return False
        
        #Validate size
        if order.size not in self.sizes:
            logger.warning(f"Invalid size detected {order.size}")
            return False
        
        #Validate price
        if not isinstance(order.price,(int,float)) or order.price <= 0 :
            logger.warning(f"Invalid price detected: {order.price}")
            return False
        
        logger.info(f"Order validated: {order.order_id}")
        return True