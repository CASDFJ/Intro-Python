from room import Room
from player import Player
import textwrap

# Declare all the rooms

# {outside: {name: "", desc: ""}}

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# d = Player(input("Where do you want to go? "))

valid_directions = {
    "n": "n",
    "s": "s",
    "e": "e",
    "w": "w",
    "forward": "n",
    "backwards": "s",
    "right": "e",
    "left": "w",
}

player = Player(input("What is your name? "), room["outside"])
print(player.currentRoom)

while True:
    # Imagine the player types in "take coins"
    # line 74 will take that input, output a string,
    # make it lowercase, and then split it between the
    # space character
    # Ultimately cmds == ['take', 'coins']
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        else:
            print("I did not understand that command.")
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
            elif cmds[1] == "room":
                # Give description of room, including items in it
        elif cmds[0] == "take":
            player.take_item(itemObjectHere)
        else:
            print("I did not understand that command.")

if (cmds[0] === 'look') {
    if (cmds[1]hasProp) {
        player.look(blah)
    }
}
else if (cmds[0] === take) {
    player.take_item()
}
