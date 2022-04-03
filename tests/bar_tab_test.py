import unittest

from classes.bar_tab import BarTab
from classes.guest import Guest
from classes.drink import Drink
from classes.loyalty_guest import LoyaltyGuest

class TestBarTab(unittest.TestCase):
    def setUp(self):
        self.bar = BarTab(50)
        self.guest = Guest("Johnny", 45, 20)
        self.loyalty_guest = LoyaltyGuest("Janie", 25, 24, 5)
        self.drink1 = Drink("Coke Zero", 1.5)
    
    def test_can_take_full_payment(self):
        self.bar.take_payment(self.guest, self.drink1)
        self.assertEqual(51.5, self.bar.value)
        self.assertEqual(43.5, self.guest.wallet)

    def test_can_take_reduced_payment(self):
        self.bar.take_payment(self.loyalty_guest, self.drink1)
        self.assertEqual(51.35, self.bar.value)
        self.assertEqual(23.65, self.loyalty_guest.wallet)