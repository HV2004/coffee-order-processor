import json
import logging
from Models.order import Order

logger = logging.getLogger(__name__)

class Reader:
    """
    Reads from a JSON file
    """

    def read(self,file_path):
        """
        Reads JSON data and converts it into order objects.
        """
        logger.info(f"Reading the input file: {file_path}")
        with open(file_path,"r") as f:
            data = json.load(f)
        orders = []
        for i in data:
            order = Order(
                order_id = i.get("order_id"),
                drink = i.get("drink"),
                size = i.get("size"),
                price = i.get("price"),
                timestamp = i.get("timestamp"),
                extras = i.get("extras")
            )
            orders.append(order)

        logger.info("Total orders read: {len(orders)}")

        return orders
    
