class Room:
    def __init__(self, name, playlist, capacity, price, bar_tab, bar_stock, guests = []):
        self.name = name
        self.playlist = playlist
        self.capacity = capacity
        self.price = price
        self.bar_tab = bar_tab
        self.bar_stock = bar_stock
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
    
    def check_stock(self, drink_to_check):
        return self.bar_stock[drink_to_check]

    def can_serve(self, guest, drink):
        if guest.check_old_enough() == False:
            return False, "Go home, kid!"
        if self.check_stock(drink) == 0:
            return False, "Sorry, we're all out of that"
        return True, ""

    def make_a_sale(self, guest, drink):
        if self.can_serve(guest, drink)[0]:
            self.bar_tab.take_payment(guest, drink)
        else:
            return self.can_serve(guest, drink)[1]
    
    def restock_drinks(self, drink, quantity = 1):
        if drink in self.bar_stock:
            self.bar_stock[drink] += quantity
        else:
            self.bar_stock[drink] = quantity