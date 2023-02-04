class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def title_by_artist(self):
        return f"{self.title} by {self.artist}"