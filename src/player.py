# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
import datetime


class Player:
    def __init__(self, room: Room, name: str):
        self.room = room
        self.name = name
        return

    def move(self, direction: str):
        print("NOT IMPLEMENTED")
        raise NotImplementedError("please wait unitl the feature is implemented")


class PlayerBag:
    def __init__(self, size: int, player: Player):
        self.size = size
        self.player = player
        self.inventory = {
            "player_name": self.player.name,
            "time_created": datetime.time(),
            "size": self.size,
            
        }
