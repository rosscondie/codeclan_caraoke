import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("The Glitter Room")
        self.room_2 = Room("The Basement Room")
        self.room_3 = Room("The Rock Room")
        self.guest_1 = Guest("Jimi Hendrix")
        self.guest_2 = Guest("Bruce Springsteen")
        self.guest_3 = Guest("Frank Sinatra")
        self.song = Song("Welcome to the Jungle", "Guns N' Roses")
        self.song = Song("Rocket Man", "Elton John")
        self.song = Song("Ice Ice Baby", "Vanilla Ice")



    def test_room_has_name(self):
        expected = "The Glitter Room"
        actual = self.room_1.name
        self.assertEqual(expected, actual)

    def test_room_has_songs(self):
        expected = []
        actual = self.room_1.songs
        self.assertEqual(expected, actual)