import unittest

from classes.karaoke_club import KaraokeClub
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestKaraokeClub(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Doreen Day", 140)
        self.guest2 = Guest("Maggie Munroe", 500)
        self.guest3 = Guest("Freddy Sinatra", 25)
        self.guest4 = Guest("Jimmy Cash", 125)
        self.guest5 = Guest("Frankie Mercury", 55)
        self.guest6 = Guest("Judy Mitchell", 110)
        self.guest7 = Guest("John Morrison", 10)
        all_guests = [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5, self.guest6, self.guest7]
        self.room1 = Room("Radio Star", [], 10, 12, 50)
        self.room2 = Room("Sing Sing", [], 15, 5, 50)
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
    
    def test_can_deny_entry(self):
        result = self.club.admit_guest(self.guest7, self.room1)
        self.assertEqual("Sorry, looks like you don't have enough money.", result)
        