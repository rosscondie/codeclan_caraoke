import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("The Glitter Room")
        self.room_2 = Room("The Rock Room")
        self.guest_1 = Guest("Jimi Hendrix")
        self.guest_2 = Guest("Bruce Springsteen")
        self.song_1 = Song("Welcome to the Jungle", "Guns N' Roses")
        self.song_2 = Song("Rocket Man", "Elton John")

    def test_room_has_name(self):
        expected = "The Glitter Room"
        actual = self.room_1.name
        self.assertEqual(expected, actual)

    def test_room_has_songs(self):
        expected = []
        actual = self.room_1.songs
        self.assertEqual(expected, actual)

    def test_can_add_songs(self):
        song = Song("Paint it Black", "The Rolling Stones")
        self.room_1.add_song(song)
        expected = song
        actual = self.room_1.songs[0]
        self.assertEqual(expected, actual)

    def test_can_add_song_to_rock_room(self):
        song = Song("Sabbra Cadabra", "Metallica")
        self.room_2.add_song(song)
        expected = song
        actual = self.room_2.songs[0]
        self.assertEqual(expected, actual)


    def test_room_1_has_capacity(self):
        expected = []
        actual = self.room_1.capacity
        self.assertEqual(expected, actual)

    def test_room_1_can_add_guest(self):
        guest = Guest("Meatloaf")
        self.room_1.add_guest(guest)
        expected = guest
        actual = self.room_1.capacity[0]
        self.assertEqual(expected, actual)

    

    