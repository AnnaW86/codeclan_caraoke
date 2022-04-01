import unittest

from classes.guest import Guest
from classes.song import Song
from classes.room import Room
from classes.bar_tab import BarTab

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Johnny", 45)
        self.song1 = Song("Mr Brightside", "The Killers")
        self.song2 = Song("Lose Yourself", "Eminem")
        self.song3 = Song("It's Tricky", "Run-D.M.C.")
        room1_playlist = [self.song1, self.song2, self.song3]
        bar_tab = BarTab(50)
        self.room1 = Room("Radio Star", room1_playlist, 10, 12, bar_tab)

    def test_can_pay(self):
        self.guest1.pay_for_something(12)
        self.assertEqual(33, self.guest1.wallet)
    
    def test_can_cheer_favourite(self):
        result = self.guest1.cheer_favourite_song("It's Tricky", self.room1)
        self.assertEqual("Whoo, this is my song!", result)
