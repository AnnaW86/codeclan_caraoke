import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.bar_tab import BarTab
from classes.drink import Drink

class TestRoom(unittest.TestCase):
    pass

    def setUp(self):
        self.guest1 = Guest("Doreen Day", 140, 24)
        self.guest2 = Guest("Maggie Munroe", 500, 18)
        self.guest3 = Guest("Freddy Sinatra", 25, 31)
        self.guest4 = Guest("Jimmy Cash", 125, 17)
        self.guest5 = Guest("Frankie Mercury", 55, 22)
        self.guest6 = Guest("Judy Mitchell", 110, 29)
        self.guest7 = Guest("John Morrison", 10, 54)
        room2_guests = [self.guest2, self.guest3, self.guest4, self.guest5, self.guest6]
        self.song1 = Song("Mr Brightside", "The Killers")
        self.song2 = Song("Lose Yourself", "Eminem")
        self.song3 = Song("It's Tricky", "Run-D.M.C.")
        room2_playlist = [self.song1, self.song2]
        self.bar_tab = BarTab(50)
        self.drink1 = Drink("Coke Zero", 1.5)
        self.drink2 = Drink("white wine", 5)
        self.drink3 = Drink("gin and tonic", 6.5)
        self.drink4 = Drink("red wine", 5)
        self.drink5 = Drink("beer", 5.5)
        self.drinks = {
            self.drink1: 50,
            self.drink2: 35,
            self.drink3: 40,
            self.drink4: 35,
            self.drink5: 60}
        self.room1 = Room("Radio Star", [self.song3], 10, 12, self.bar_tab, self.drinks)
        self.room2 = Room("Sing Sing", room2_playlist, 5, 15, self.bar_tab, self.drinks, room2_guests)


    def test_can_add_guest(self):
        self.room1.check_in(self.guest1)
        self.assertEqual(self.guest1.name, self.room1.guests[0].name)

    def test_can_remove_guest(self):
        self.room2.check_out(self.guest3)
        self.assertEqual(self.room2.guests[1], self.guest4)
        self.assertEqual(4, len(self.room2.guests))

    def test_can_add_songs(self):
        self.room2.add_song(self.song3)
        self.assertEqual(self.room2.playlist[2], self.song3)
    
    def test_can_make_sale(self):
        self.room2.make_a_sale(self.guest2, self.drink4)
        self.assertEqual(495, self.guest2.wallet)
        self.assertEqual(55, self.room2.bar_tab.value)

    def test_can_restock_drink(self):
        self.room1.restock_drinks(self.drink1)
        self.assertEqual(51, self.drinks[self.drink1])
    
    def test_can_add_new_drink(self):
        drink6 = Drink("Coke", 1.8)
        self.room1.restock_drinks(drink6, 50)
        self.assertEqual(50, self.drinks[drink6])