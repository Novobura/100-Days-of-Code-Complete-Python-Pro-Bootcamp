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

choice1 = input('You walk up to the jungle tree line from the beach, leaving your boat near the surf. The sun beats down from above, a blistering day on the equator. The din of the waves fades as the breath of the jungle, the birds and insects, grows louder. You see a forked path into the foliage. Do you go left or right?').lower()


if choice1 == "left":
    choice2 = input('You enter the jungle and as you process some yards the sun grows brighter and it becomes easier to see. The sound of animals grows louder and you see a clearing uphead. As you enter the clearing you see fresh water and green grass. As you aporach the water you see the rotting skeletal remains of a long dead pirate. You pick up his cutlass. You progress toward the water. Do you swim or wait?').lower()
    if choice2 == "swim":
      choice3 = input("You enter the clear fresh water and swim across to the other side, up ahead you see a house with 3 doors. One is red, one is yellow and one blue. Which do you choose?")
      if choice3 == "red":
        print('You open the door and are attacked by a walking rock creature. You swing your cutlass but its too hard, the rock creature bash your head in. Game over.')
      elif choice3 == "yellow":
        print('Ye found the gold debloons. Ye win!')
      elif choice3 == "blue":
        print('You open the door and are attacked by a walking shark, as it lunges at you, you swing your cutlass and slice off its head. The door slams shut as your attacked and devoured by its young. Game over.')
      else:
        print('As you daddle outside, the sun goes down, you hear a moaning and a rotting smell. You are attacked by a hoard of zombies that stumble from the tree line. You swing your cutlas but its too late, the zombies have ye')
    else:
      print('You see a shape in the sky like a bird. You see it get bigger and realize its a gargantuan bird. You try to run but it is too late, it swoops down and has ye. Game Over.')
  
else:
  print('You enter the jungle but as you progress some yards the light of day fades and it becomes difficult to see. The sound of animals grows quiet and you hear a loud snap behind you as if being stalked by a predator. You sprint forward in panic, and you hear a bone shaking roar. Without looking you fall down a cragy precipise into an underground tunnel. The world goes dark. Game over.')