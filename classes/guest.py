class Guest:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
    
    def pay_for_something(self, item):
        self.wallet -= item.price
    
    def check_old_enough(self):
        return self.age >= 18

    def check_has_funds(self, room):
        return self.wallet >= room.price

    def cheer_favourite_song(self, favourite_song, room):
        for song in room.playlist:
            if song.name == favourite_song:
                return "Whoo, this is my song!"