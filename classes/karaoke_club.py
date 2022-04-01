class KaraokeClub:
    def __init__(self, name, rooms, guests, till = 0):
        self.name = name
        self.rooms = rooms
        self.guests = guests
        self.till = till
    
    def take_money(self, room):
        self.till += room.price
    
    def check_guest_can_be_admitted(self, guest, room):
        if room.check_capacity() == False:
            return False, f"Sorry, {room.name} is full, do you want to try another?"
        if guest.wallet < room.price:
            return False, f"Sorry, looks like you don't have enough money."
        return True, ""
            
    def admit_guest(self, guest, room):
        if self.check_guest_can_be_admitted(guest, room)[0]:
            room.check_in(guest)
            guest.pay_for_something(room.price)
            self.take_money(room)
        else:
            return self.check_guest_can_be_admitted(guest, room)[1]