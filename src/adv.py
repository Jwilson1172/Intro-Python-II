from player import Player, PlayerBag
from routes import Route

#
# Main
#
# starting the world map up and getting all of the routes for movement set up.
world_map = Route()
room = world_map.room

mainoc = Player(room["outside"], "Generic Playername")
bag = PlayerBag(20, mainoc)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def print_room():
    print(
        "{} is in room {}, {}\n\n".format(
            mainoc.name, mainoc.room.name, mainoc.room.description
        )
    )
    return


# print when a player decides to try to go through a wall
def print_void():
    print("you can't go that direction sorry")
    return


def print_end():
    print(
        "\n\n*****************************\n",
        "\tYOU DIED :(\n",
        "*****************************\n",
    )
    return


DBG = True
while True:
    # I want to make sure that i catch any straggler exceptions
    try:
        # print the current room then ask the user to imput a command
        print_room()
        exit()
        # adding a fail condition to the game
        if mainoc.room.id == 5:
            print_end()
        # get user input
        user_input = input(
            "please enter the direction that you wouldf like to go [n,s,e,w] or q to quit: "
        ).lower()

        # respond to user input
        # case cardinal directions
        if user_input in ["n", "s", "e", "w"]:
            # bit of dbg
            if DBG:
                print("\nuser inputed:{}\n\n".format(user_input))
            try:
                # checks the direction cases and evalueates if that room has a
                # room in the direction that the user requests
                # if both of those conditions are true then assign the player's
                # to the new room that is selected
                if (user_input == "w") & (mainoc.room.w_to is not None):
                    mainoc.room = mainoc.room.w_to
                elif (user_input == "n") & (mainoc.room.n_to is not None):
                    mainoc.room = mainoc.room.n_to
                elif (user_input == "s") & (mainoc.room.s_to is not None):
                    mainoc.room = mainoc.room.s_to
                elif (user_input == "e") & (mainoc.room.e_to is not None):
                    mainoc.room = mainoc.room.e_to

            except Exception as e:
                if DBG:
                    print(e)
                print_void()

        # quit condition
        elif user_input == "q":
            quit_confirm = input("are you sure? [y/n]").lower()
            if quit_confirm == "y":
                exit()
        # unknown command input
        else:
            print("that command was not understood please try again\n")

    # unknown error occured in the loop that isn't caught by anything
    except Exception as e:
        print(e)
        exit(1)
