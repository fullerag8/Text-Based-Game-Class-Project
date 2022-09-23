# Angela Fuller

# Game greeting and instructions
def show_instructions():
    print('Welcome to the Cat Text Adventure Game!')
    print('Collect all 6 items to keep you safe from the vacuum cleaner - and maybe even destroy it for good!')
    print('Move commands: go North, go South, go East, go West')
    print("Add items to inventory: get 'item name'")
# current room and inventory status
def show_status():
    print('You are in the ', current_room)
    print('Inventory: ', current_inventory)
# text for if player loses
def loser_text():
    print('The Vacuum roars to life')
    print('You realize too late that you are not prepared to defeat it with all 6 items!')
    print('You lose! Try again.')
# text for if player wins
def victory_text():
    print('You look at the Vacuum head on as it roars to life.')
    print('You eat your treat to give you strength.')
    print('You throw your Mouse Toy, Feather Wand, and Fluffy Blanket in its path.')
    print('As the Vacuum sucks up the toys, you cower with your Stuffed Rabbit in the Cardboard Box.')
    print('The Fluffy Blanket finally stops the loud rumble.')
    print('The Vacuum has been defeated once and for all! You Win!')


# The dictionary links a room to other rooms and items to rooms.
rooms = {
        'Living Room': {'South': 'Basement', 'North': 'Office', 'West': 'Kitchen', 'East': 'Bedroom'},
        'Kitchen': {'East': 'Living Room', 'item': 'Treat'},
        'Bedroom': {'West': 'Living Room', 'North': 'Bathroom', 'item': 'Stuffed Rabbit'},
        'Bathroom': {'South': 'Bedroom', 'item': 'Mouse Toy'},
        'Office': {'South': 'Living Room', 'East': 'Sunroom', 'item': 'Feather Wand'},
        'Sunroom': {'West': 'Office', 'item': 'Fluffy Blanket'},
        'Basement': {'North': 'Living Room', 'East': 'Utility Room', 'item': 'Cardboard Box'},
        'Utility Room': {'West': 'Basement', 'item': 'Vacuum'}
    }

moving_directions = ['go North', 'go South', 'go East', 'go West']
item_directions = ['get Treat', 'get Stuffed Rabbit', 'get Mouse Toy', 'get Feather Wand', 'get Fluffy Blanket', 'get Cardboard Box']
# start in living room
current_room = 'Living Room'
current_inventory = []

show_instructions()

# game loop
while True:
    # print current location and inventory
    show_status()
    if 'item' in list(rooms[current_room].keys()) and rooms[current_room]['item'] not in current_inventory:
        print('You see a', rooms[current_room]['item'])
    # request user input
    print('Enter your move:')
    command = input()
    if command in moving_directions:
        # separate go from direction
        player_direction = command.split(' ')[1]
        if player_direction in rooms[current_room]:
            # assigning new current room
            current_room = rooms[current_room][player_direction]
            # check how many items are in inventory
            number_items = len(current_inventory)
            if current_room == 'Utility Room':
                # check if you have all 6 items to win
                if number_items <6:
                    # if not, they lose
                    loser_text()
                    break
                else:
                    # if so, they win!
                    victory_text()
                    break
        else:
            # message for invalid direction
            print("You can't go that way!")
    # Adding items to inventory
    elif command in item_directions:
        player_item = command.split(' ', 1)[1]
        # check if item is valid, and in correct room
        if player_item not in current_inventory and rooms[current_room]['item'] == player_item:
            # add to inventory
            current_inventory.append(player_item)
            print(player_item, 'retrieved!')
        else:
            print('Unable to retrieve', player_item)
    else:
        # for when the input is not a direction
        print('Invalid command')
