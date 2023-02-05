class Room:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.capacity = []

    def add_song(self, new_song):
        self.songs.append(new_song)

    def add_guest(self, new_guest):
        self.capacity.append(new_guest)