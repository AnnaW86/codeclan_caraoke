class BarTab:
    def __init__(self, value = 0):
        self.value = value

    def add_to_tab(self, amount):
        self.value += amount
    
    def take_payment(self, amount, guest):
        self.add_to_tab(amount)
        guest.pay_for_something(amount)
