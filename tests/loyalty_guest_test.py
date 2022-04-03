import unittest

from classes.loyalty_guest import LoyaltyGuest

class TestLoyaltyGuest(unittest.TestCase):
    def setUp(self):
        self.loyalty_guest1 = LoyaltyGuest("Kenny Minogue", 450, 35, 6)
    
    def test_guest_has_loyalty_tally(self):
        self.assertEqual(6, self.loyalty_guest1.loyalty_tally)