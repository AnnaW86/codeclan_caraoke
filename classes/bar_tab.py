class BarTab:
    def __init__(self, value = 0):
        self.value = value

    def add_to_tab(self, item):
        self.value += item.price
    
    def take_payment(self, guest, item):
        self.add_to_tab(item)
        guest.pay_for_something(item)
