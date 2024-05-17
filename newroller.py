import random, os, time
die     = ["   \n   \n   "]   #nothing
die.append("   \n O \n   ")   #1
die.append("  O\n   \nO  ")   #2
die.append("O  \n   \n  O")   #3
die.append("O O\n O \nO O")   #4
die.append("O O\nO O\nO O")   #5
die.append("O O\nO O\nO O")   #6
die.append("O O\nO O\nO O\nO") #7
die.append("O O\nO O\nO O\nO O") #8
die.append("O O\nO O\nO O\nO O\nO") #9
die.append("O O\nO O\nO O\nO O\nO O") #10
die.append("O O\nO O\nO O\nO \nO O\nO") #11
die.append("O O\nO O\nO O\nO O\nO O\nO O") #12
die.append("O O\nO O\nO O\nO O\nO O\nO O\nO") #13
die.append("O O\nO O\nO O\nO O\nO O\nO O\nO O") #14
die.append("O O\nO O\nO O\nO O\nO O\nO O\nO O\nO") #15
die.append("O O\nO O\nO O\nO O\nO O\nO O\nO O\nO O") #16
die.append("O O\nO O\nO O\nO O\nO O\nO O\nO O\nO O\nO") #17
die.append("O O\nO O\nO O\nO O\nO O\nO O\nO O\nO O\nO O") #18
die.append("O O\nO O\nO O\nO O\nO O\nO O\nO O\nO O\nO O\nO") #19
die.append("O O\nO O\nO O\nO O\nO O\nO O\nO O\nO O\nO O\nO O") #20



def dice_roller(sides):
  roll=random.randrange(sides)
  #uncomment line below to see the number
  #print(roll+1)
  return(roll+1)



def animate_die(sides, num_of_dice):
    total=0
    for roll in range(0,num_of_dice):
        #os.system('cls')
        print("/n")
        number = dice_roller(sides)
        total+=number
        print(die[number])
        time.sleep(1)
    print("\nTotal: ",total)
    return total

animate_die(6,3)
