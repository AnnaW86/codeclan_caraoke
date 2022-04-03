class KaraokeClub:
    def __init__(self, name, rooms, guests, till = 0):
        self.name = name
        self.rooms = rooms
        self.guests = guests
        self.till = till
    
    def take_money(self, item):
        self.till += item.price

    def check_guest_can_be_admitted(self, guest, room):
        if room.check_capacity() == False:
            return False, f"Sorry, {room.name} is full, do you want to try another?"
        if guest.check_has_funds(room) == False:
            return False, f"Sorry, looks like you don't have enough money."
        if guest.check_old_enough() == False:
            return False, f"Sorry, kid, go home!"
        return True, ""

    def admit_guest(self, guest, room):
        room.check_in(guest)
        guest.pay_for_item(room)
        self.take_money(room)
        if hasattr(guest, 'loyalty_tally'):
            guest.increase_loyalty_tally()

    def admit_regular_guest(self, guest, room):
        if self.check_guest_can_be_admitted(guest, room)[0]:
            self.admit_guest(guest, room)
        else:
            return self.check_guest_can_be_admitted(guest, room)[1]
    

    def admit_loyalty_guest(self, loyalty_guest, room):
        if self.check_guest_can_be_admitted(loyalty_guest, room)[0]:
            if loyalty_guest.loyalty_tally <=9:
                self.admit_guest(loyalty_guest, room)
                if loyalty_guest.loyalty_tally == 10:
                    return "Next one's free!"
            if loyalty_guest.loyalty_tally == 10:
                room.check_in(loyalty_guest)
                loyalty_guest.loyalty_tally = 0
        else:
            return self.check_guest_can_be_admitted(loyalty_guest, room)[1]
