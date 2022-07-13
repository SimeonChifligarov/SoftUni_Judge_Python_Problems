from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(name=f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        current_room = self.__find_room_by_number(room_number)
        if not current_room.is_taken and current_room.capacity >= people:
            self.guests += people
        current_room.take_room(people)

    def free_room(self, room_number):
        current_room = self.__find_room_by_number(room_number)
        if current_room.is_taken:
            self.guests -= current_room.guests
        current_room.free_room()

    def status(self):
        result = []
        free_rooms_numbers_as_str = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms_numbers_as_str = [str(r.number) for r in self.rooms if r.is_taken]

        result.append(f'Hotel {self.name} has {self.guests} total guests')
        result.append(f'Free rooms: {", ".join(free_rooms_numbers_as_str)}')
        result.append(f'Taken rooms: {", ".join(taken_rooms_numbers_as_str)}')
        return '\n'.join(result)

    def __find_room_by_number(self, room_number):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        return current_room
