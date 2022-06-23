from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name not in [a.name for a in self.albums]:
            return f"Album {album_name} is not found."

        current_album = [a for a in self.albums if a.name == album_name][0]
        if current_album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(current_album)
        return f"Album {album_name} has been removed."

    def details(self):
        details_result = f"Band {self.name}\n"
        for album in self.albums:
            details_result += f"{album.details()}\n"

        return details_result.strip()
