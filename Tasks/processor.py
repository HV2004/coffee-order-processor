class Processor:
    def process(self,order):
        return [order.order_id,order.drink,order.size,f"{order.price:.2f}",order.timestamp_case(),order.extras_count()]