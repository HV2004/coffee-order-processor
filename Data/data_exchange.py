class DataStorage:
    """
    Central data storage class used across the task
    """
    def __init__(self):
        self.orders = []
        self.processed_orders = []
        self.analytics = {}
        self.exchange_rate = None
        self.currency = "USD"

    def set_orders(self,orders):
        self.orders = orders
    
    def get_orders(self):
        return self.orders
    
    def set_processed_orders(self,orders):
        self.processed_orders = orders
        
    def get_processed_orders(self):
        return self.processed_orders
    
    def set_exchange_rate(self,rate):
        self.exchange_rate = rate

    def get_exchange_rate(self):
        return self.exchange_rate
    
    def set_currency(self,currency):
        self.currency = currency

    def get_currency(self):
        return self.currency
    