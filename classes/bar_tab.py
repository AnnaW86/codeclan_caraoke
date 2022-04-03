class BarTab:
    def __init__(self, value = 0):
        self.value = value

    def add_to_tab(self, amount):
        self.value += amount

    def take_payment(self, guest, item):
        amount = guest.pay_for_drink(item)
        self.add_to_tab(amount)
