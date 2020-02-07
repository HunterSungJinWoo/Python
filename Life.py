import time
health= 100
play = True

def print_health(hp):
    l='■'
    s='|'
    for i in range(10):
        if i<hp/10:
          s+=l # show a bar of health if multiple of 10
        else:
          s+=" " # else fill the missing hp with space
        if i%2==1:
          s+='|' # print a | every 2 characters
    print(s)

while play:
  try:
      damage= int(input("How much damage would you like to take?" ))
  except ValueError:
      print("That isn't a command")
      continue # starts the loop over
  remaining_health = health - damage
  print("You took {0} damage!".format(damage))
  health=remaining_health
  print(" --------------")
  print_health(remaining_health)
  print(" --------------")

  if remaining_health <= 0:
    print("You died!")
    break # exit the loop

  again = 'x'
  while again not in 'YN': # you may want to cast againt to upper
      again = input("Would you like to play again? |Y/N| ")
      if again == "N":
        play = False
      elif again != 'Y':
        print("That is not a command...")
print("The program will now close")
time.sleep(5)
