#mainline logic
def housekeeping():
    print("housekeeping")

def detailloop():
    print("Detail loop")
    global loopnum
    loopnum-=1

def endofjob():
    print("End of job")
    print("byeeeeeeeeeeee")
#main
myvar=""
global loopnum
loopnum=100
housekeeping()
while loopnum>0:
    detailloop()
endofjob()
