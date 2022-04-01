class Room:
    def __init__(self, name, playlist, capacity, price, bar_tab, guests = []):
        self.name = name
        self.playlist = playlist
        self.capacity = capacity
        self.price = price
        self.bar_tab = bar_tab
        self.guests = guests


    
    def check_capacity(self):
        return len(self.guests) < self.capacity

    def check_in(self, guest):
        self.guests.append(guest)
    
    def check_out(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)
    
    def add_song(self, new_song):
        if new_song not in self.playlist:
            self.playlist.append(new_song)
    
    def make_a_sale(self, amount, guest):
        self.bar_tab.take_payment(amount, guest)
    