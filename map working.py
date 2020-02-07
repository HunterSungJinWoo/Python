def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========

Get to the Garden with a key, a knife and a matchbox
But beware of the monsters!

Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east'  : 'Living Room',
                  'item'  : 'knife'
                },
            'Dining Room' : {
                  'west'  : 'Hall',
                  'south' : 'Living Room',
                  'east'  : 'Garden',
                  'item'  : 'matchbox'
                },
            'Living Room' : {
                  'north' : 'Dining Room',
                  'west'  : 'Kitchen',
                  'item'  : 'monster'
                },
            'Garden' : {
                  'west'  : 'Dining Room'
            }

         }

# Displays a map of all the accesable rooms from the current room.
def room_map():

  # Makes sure that a variable defaults to an empty string...
  # ...if the current room doesnt link to another room in that direction.
  try:
    north = rooms[currentRoom]['north']
  except:
    north = ""
  try:
    south = rooms[currentRoom]['south']
  except:
    south = ""
  try:
    east = rooms[currentRoom]['east']
  except:
    east = ""
  try:
    west = rooms[currentRoom]['west']
  except:
    west = ""

  # Prints the map
  n = "N"
  s = "S"
  vert_line = "|"
  hzt_line = "-- W -- X -- E --"
  print(north.center(30))
  print("")
  print(vert_line.center(30))
  print(n.center(30))
  print(vert_line.center(30))
  print(west + hzt_line.center(30 - len(west) * 2) + east)
  print(vert_line.center(30))
  print(s.center(30))
  print(vert_line.center(30))
  print("")
  print(south.center(30))
  print("")

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
  room_map()
  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')

  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  # player loses if they enter a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you....GAME OVER!')
    break

  # player wins if they get to the garden with a key, a matchbox and a knife
  if currentRoom == 'Garden' and 'key' in inventory and 'matchbox' in inventory and 'knife' in inventory:
    print('You escaped the house... YOU WIN!')
    break
