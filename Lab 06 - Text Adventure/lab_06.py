class Room:
    """
    This class represents the room.
    """
    def __init__(self, description, south, west, north, east):
        self.description = description
        self.north = north
        self.east = east
        self.west = west
        self.south = south


def main():
    room_list = []
    my_room = Room("You are here starting in the kids' bedroom. There is one door to the north and one door to the \n"
                   "east.", None, None,
                   3, 1)
    room_list.append(my_room)

    my_room = Room("You are in the living room. In here, there is a lamp and couch to the south. Doors are located \n"
                   "west,east, and north of you.", None, 0, 2, 6)
    room_list.append(my_room)

    my_room = Room("You are in the bathroom. The sink is north of you. Therefore you can only travel east, south, or \n"
                   "west.", 1, 3, None, 5)
    room_list.append(my_room)

    my_room = Room("You are in the kitchen and dining room now. Your appliances are located only to the north. \n"
                   "You can either travel south, east, or west.", 0, 4, None, 2)
    room_list.append(my_room)

    my_room = Room("You are in the master bedroom. There is one door to the east. ", None, None,
                   None, 3)
    room_list.append(my_room)

    my_room = Room("You are in the game room. Stay and play games or travel either west or south.", 6, 2, None, None)
    room_list.append(my_room)

    my_room = Room("You are outside on the patio. Enjoy the view and stay awhile. Otherwise, go back inside \n"
                   "towards the living room to the west or head north to the game room.", None, 1, 5, None)
    room_list.append(my_room)

    current_room = 0

    done = False
    while not done:

        print()
        print(room_list[current_room].description)
        user_input = input("What do you want to do? ")
        if user_input.lower() == "q" or user_input.lower() == "quit":
            print("Thank you for playing.")
            break

        if user_input.lower() == "north" or user_input.lower() == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "south" or user_input.lower() == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "west" or user_input.lower() == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "east" or user_input.lower() == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room


main()