number=1
while(number<=10):
    print(number)
    number=number+1

number=5
while(number<=15):
    print(number)
    number=number+1


def housekeeping():
    print("housekeeping")

def detailloop():
    print("Detail loop")
    global loopnum
    loopnum-=1
