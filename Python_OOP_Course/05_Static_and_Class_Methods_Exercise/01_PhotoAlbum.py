import math


class PhotoAlbum:
    PAGE_SEPARATION = "-" * 11
    PHOTO_MARKED_AS = "[]"
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages_needed = math.ceil(photos_count / PhotoAlbum.MAX_PHOTOS_PER_PAGE)
        return cls(pages_needed)

    def add_photo(self, label: str):
        if len(self.photos[-1]) >= PhotoAlbum.MAX_PHOTOS_PER_PAGE:
            return "No more free slots"

        for idx in range(len(self.photos)):
            for ph_idx in range(PhotoAlbum.MAX_PHOTOS_PER_PAGE):
                if ph_idx == len(self.photos[idx]):
                    self.photos[idx].append(label)
                    return f"{label} photo added successfully on page {idx+1}" \
                           f" slot {ph_idx+1}"

    def display(self):
        display_result = [PhotoAlbum.PAGE_SEPARATION]
        for idx in range(len(self.photos)):
            current_page = self.photos[idx]
            current_page_result = [PhotoAlbum.PHOTO_MARKED_AS for _ in current_page]
            display_result.append(" ".join(current_page_result))
            display_result.append(PhotoAlbum.PAGE_SEPARATION)

        return "\n".join(display_result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
