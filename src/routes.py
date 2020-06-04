from room import Room


class Route:
    # Declare all the rooms
    def __init__(self):
        self.room = {
            "outside": Room(
                0, "Outside Cave Entrance", "North of you, the cave mouth beckons"
            ),
            "foyer": Room(
                1,
                "Foyer",
                """Dim light filters in from the south. Dusty
                            passages run north and east.""",
            ),
            "overlook": Room(
                2,
                "Grand Overlook",
                """A steep cliff appears before you, falling
                            into the darkness. Ahead to the north, a light flickers in
                            the distance, but there is no way across the chasm.""",
            ),
            "narrow": Room(
                3,
                "Narrow Passage",
                """The narrow passage bends here from west
                            to north. The smell of gold permeates the air.""",
            ),
            "treasure": Room(
                4,
                "Treasure Chamber",
                """You've found the long-lost treasure
                            chamber! Sadly, it has already been completely emptied by
                            earlier adventurers. The only exit is to the south.""",
            ),
            "monster": Room(
                5,
                "Monster Chamber",
                "as the player enters this room there is a snarl from the corner of the \
                    room before you have time to react a cursed creture lunges at you\n",
            ),
        }
        # Link rooms together
        # look into random assignment of the room map

        self.room["outside"].n_to = self.room["foyer"]
        self.room["foyer"].s_to = self.room["outside"]
        self.room["foyer"].n_to = self.room["overlook"]
        self.room["foyer"].e_to = self.room["narrow"]
        self.room["overlook"].s_to = self.room["foyer"]
        self.room["narrow"].w_to = self.room["foyer"]
        self.room["narrow"].n_to = self.room["treasure"]
        self.room["treasure"].s_to = self.room["narrow"]
        self.room["monster"].s_to = self.room["treasure"]
        self.room["treasure"].n_to = self.room["monster"]
