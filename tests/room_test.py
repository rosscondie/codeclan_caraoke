import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Glitter Room")

    def test_room_has_name(self):
        expected = "Glitter Room"
        actual = self.room.name
        self.assertEqual(expected, actual)

    def test_room_has_songs(self):
        expected = []
        actual = self.room.songs
        self.assertEqual(expected, actual)