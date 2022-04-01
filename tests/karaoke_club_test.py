import unittest

from classes.karaoke_club import KaraokeClub
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink

class TestKaraokeClub(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Doreen Day", 140, 24)
        self.guest2 = Guest("Maggie Munroe", 500, 18)
        self.guest3 = Guest("Freddy Sinatra", 25, 31)
        self.guest4 = Guest("Jimmy Cash", 125, 17)
        self.guest5 = Guest("Frankie Mercury", 55, 22)
        self.guest6 = Guest("Judy Mitchell", 110, 29)
        self.guest7 = Guest("John Morrison", 10, 54)
        all_guests = [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5, self.guest6, self.guest7]
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
        self.room1 = Room("Radio Star", [], 10, 12, 50, self.drinks)
        self.room2 = Room("Sing Sing", [], 15, 5, 50, self.drinks)
        self.room3 = Room("Solo Star", [], 1, 40, 50, self.drinks)
        all_rooms = [self.room1, self.room2]
        self.club = KaraokeClub("The Club", all_rooms, all_guests)
    
    def test_can_take_money(self):
        self.club.take_money(self.room1)
        self.assertEqual(12, self.club.till)

    def test_can_admit_guest_to_room(self):
        self.club.admit_guest(self.guest1, self.room1)
        self.assertEqual(self.guest1, self.room1.guests[0])
        self.assertEqual(12, self.club.till)
        self.assertEqual(128, self.guest1.wallet)
    
    def test_can_deny_entry__no_funds(self):
        result = self.club.admit_guest(self.guest7, self.room1)
        self.assertEqual("Sorry, looks like you don't have enough money.", result)
     
    def test_can_deny_entry__too_young(self):
        result = self.club.admit_guest(self.guest4, self.room1)
        self.assertEqual("Sorry, kid, go home!", result)
    
    def test_can_deny_entry__room_full(self):
        self.room3.guests.append(self.guest1)
        result = self.club.admit_guest(self.guest2, self.room3)
        self.assertEqual("Sorry, Solo Star is full, do you want to try another?", result)

        