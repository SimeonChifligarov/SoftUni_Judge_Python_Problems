from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = [*songs] if not [*songs] == [None] else []
        self.published = False

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."

        if self.published:
            return "Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        if song_name not in [s.name for s in self.songs]:
            return "Song is not in the album."

        for s in self.songs:
            if s.name == song_name:
                self.songs.remove(s)
                return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        details_result = f"Album {self.name}\n"
        for current_song in self.songs:
            details_result += f"== {current_song.get_info()}\n"

        return details_result.strip()
