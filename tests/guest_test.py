import unittest 
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Tupac Shakur")

    def test_guest_has_name(self):
        expected = "Tupac Shakur"
        actual = self.guest.name
        self.assertEqual(expected, actual)