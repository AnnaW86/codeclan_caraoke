class Guest:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.discount_rate = 1
    
    def pay_for_item(self, item):
        self.wallet -= item.price
    
    def pay_for_drink(self, item):
        amount = item.price * self.discount_rate
        self.wallet -= amount
        return amount
    
    def check_old_enough(self):
        return self.age >= 18

    def check_has_funds(self, room):
        return self.wallet >= room.price

    def cheer_favourite_song(self, favourite_song, room):
        for song in room.playlist:
            if song.name == favourite_song:
                return "Whoo, this is my song!"