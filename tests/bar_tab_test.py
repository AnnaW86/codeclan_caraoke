import unittest

from classes.bar_tab import BarTab
from classes.guest import Guest

class TestBarTab(unittest.TestCase):
    def setUp(self):
        self.bar = BarTab(50)
        self.guest = Guest("Johnny", 45)
    
    def test_can_take_payment(self):
        self.bar.take_payment(15, self.guest)
        self.assertEqual(65, self.bar.value)
        self.assertEqual(30, self.guest.wallet)