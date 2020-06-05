# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
import datetime


class Player:
    def __init__(self, room: Room, name: str):
        self.room = room
        self.name = name
        return

    def printStat(self):
        pass


class PlayerBag:
    def __init__(self, size: int, player: Player):
        self.size = size
        self.player = player
        self.inventory = {
            "player_name": self.player.name,
            "time_created": datetime.time(),
            "size": self.size}

    def add(self, item ):
        if len(self.inventory.keys()) < self.size:
            self.inventory.values.append()

    def drop(self):
        pass

    def print_inv(self):
        pass
