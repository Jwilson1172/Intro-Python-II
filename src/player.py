# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, room: Room, name: str):
        self.room = room
        self.name = name
        return

    def move(self, direction: str):
        print("NOT IMPLEMENTED")
        raise NotImplementedError("please wait unitl the feature is implemented")
