from classes.guest import Guest

class LoyaltyGuest(Guest):
    def __init__(self, name, wallet, age, loyalty_tally = 0):
        super().__init__(name, wallet, age)
        self.discount_rate = 0.9
        self.loyalty_tally = loyalty_tally
    
    def increase_loyalty_tally(self):
        self.loyalty_tally += 1

