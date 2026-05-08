class Order:
    def __init__(self,order_id,drink,size,price,timestamp,extras):
        self.order_id = order_id
        self.drink = drink
        self.size = size
        self.price = price
        self.timestamp = timestamp
        self.extras = extras
    
    def extras_count(self):
        return len(self.extras) if self.extras else 0
    
    def timestamp_case(self):
        if self.timestamp:
            return self.timestamp
        else:
            return "N/A"
        
    