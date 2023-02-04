import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Everybody", "Logic")

    def test_song_has_title(self):
        expected = "Everybody"
        actual = self.song.title
        self.assertEqual(expected, actual)

    def test_song_has_artist(self):
        expected = "Logic"
        actual = self.song.artist
        self.assertEqual(expected, actual)

    def test_can_display_title_by_artist(self):
        expected = "Everybody by Logic"
        actual = self.song.title_by_artist()
        self.assertEqual(expected, actual)
