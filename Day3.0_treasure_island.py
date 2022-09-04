print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input('Ye walk up to the jungle tree line from the beach, leaving your boat near the surf. The sun beats down from above, a blistering day on the equator. The din of the waves fades as the breath of the jungle, the birds and insects, grows louder. Ye see a forked path into the foliage. Do ye go left or right?').lower()


if choice1 == "left":
    choice2 = input('Ye enter the jungle and as ye progress some yards the sun grows brighter and it becomes easier to see. The sound of animals grows louder and ye see a clearing uphead. As ye enter the clearing ye see fresh water and green grass. As ye approach the water ye see the rotting skeletal remains of a long dead pirate. Ye pick up his cutlass. Ye progress toward the water. Do you swim or wait?').lower()
    if choice2 == "swim":
      choice3 = input("Ye enter the clear fresh water and swim across to the other side, up ahead ye see a house with 3 doors. One is red, one is yellow and one blue. Which door do ye choose?")
      if choice3 == "red":
        print("Ye open the door and are attacked by a enmourmous crab creature. Ye swing your cutlass but the creature's carapace is too hard, the crab bashes your head in. Game over.")
      elif choice3 == "yellow":
        print('Ye found the gold debloons. Ye win!')
      elif choice3 == "blue":
        print('Ye open the door and are attacked by a walking shark, as it lunges at you, you swing your cutlass and slice off its head. The door slams shut as your attacked and devoured by its young. Game over.')
      else:
        print('As ye daddle outside, the sun goes down, ye hear a moaning and a rotting smell. Ye are attacked by a hoard of zombies that stumble from the tree line. Ye swing your cutlas and fell the first ghoul but its too late, the zombies have ye. Game over.')
    else:
      print('Ye see a shape in the sky like a bird. Ye see it get bigger and realize its a gargantuan teratorn. You try to run but it is too late, it swoops down and has ye. Game Over.')
  
else:
  print('Ye enter the jungle but as ye progress some yards the light of day fades and it becomes difficult to see. The sound of animals grows quiet and ye hear a loud snap behind ye as if being stalked by a predator. Ye sprint forward in panic, and ye hear a bone shaking roar. Without looking you fall down a cragy precipise into an underground tunnel. The world goes dark. Game over.')
