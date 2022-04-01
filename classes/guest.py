class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def pay_for_something(self, amount):
        self.wallet -= amount
    
    def cheer_favourite_song(self, favourite_song, room):
        for song in room.playlist:
            if song.name == favourite_song:
                return "Whoo, this is my song!"