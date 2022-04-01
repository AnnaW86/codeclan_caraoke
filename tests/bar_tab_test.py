import unittest

from classes.bar_tab import BarTab
from classes.guest import Guest
from classes.drink import Drink

class TestBarTab(unittest.TestCase):
    def setUp(self):
        self.bar = BarTab(50)
        self.guest = Guest("Johnny", 45, 20)
        self.drink1 = Drink("Coke Zero", 1.5)
    
    def test_can_take_payment(self):
        self.bar.take_payment(self.guest, self.drink1)
        self.assertEqual(51.5, self.bar.value)
        self.assertEqual(43.5, self.guest.wallet)