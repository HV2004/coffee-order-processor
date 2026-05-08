class Valid:
    drinks = {"espresso","latte","cappuccino","americano"}
    sizes = {"small","medium","large"}

    def validate(self, order):
        if order.drink not in self.drinks:
            return False
        if order.size not in self.sizes:
            return False
        if not isinstance(order.price,(int,float)) or order.price <= 0 :
            return False
        return True