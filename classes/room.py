class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.songs = []
        self.guests = []
        self.capacity = capacity

    def add_song(self, new_song):
        self.songs.append(new_song)

    def add_guest(self, new_guest):
        self.guests.append(new_guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)

    