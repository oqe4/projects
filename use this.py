#payten bell
#your future
#0.0.1
#1/31/2024

fortune=input("do you want your fortune told").lower()
if (fortune == "yes"):
    print("goodbye go eat square cheese")
else:
    color=input("pick a color red,blue,green,orange?")
    length=len(color)
    if(length % 2 == 0): #even
        number1=input("Pick a number:1,2,7 or 8")
        number2=int(number1)
        if(number %2 == 0):
            number2=int(input("pick a number- 1,2,5 or 6"))
        else:
            number2=int(input("pick a number- 3,4,7 or 8"))

    else:#odd
        number1=(input("pick a number- 3, 4, 7 or 8"))
        number1=int(number1)
        if(number % 2 == 0):
            number2=(input("pick a number- 3, 4, 7 or 8"))
        else:
            number2=int(input("pick a number- 1,2,5 or 6"))
if (number1==1):
    print("you won't get a srt")
elif (number2==2):
    print("you won't get a cookie")
elif (number2==3):
    print("your grandma will fall down the stairs")
elif (number2==3):
    print("you will stub your toe")
elif (number2==4):
    print("you won't get candy")
elif (number2==5):
    print("you will die")
elif (number2==6):
    print("you will loose a finger")
elif (number2==7):
    print("you won't make it into the fncs")
elif (number2==8):
    print("you will never win a nitro type game again")
