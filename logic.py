#mainline logic
def housekeeping():
    print("housekeeping\n******")
    print("heading: program is starting")
    print("Opening a file...")
    global file
    file=open("name.txt")
    print("reading first item from file..")
    name=file.readLine().upper()
    print(name)

def detailloop():
    print("Detail loop\n******")
    global loopnum
    global file
    print("Reading next item from file...")
    name=file.readline().upper()
    print(name)
    loopnum-=1

def endofjob():
    print("end of job\n********")
    print("closing file")
    global file
    file.close()
    print("footer: program is done")

#main
myvar=""
global loopnum, name, file

loopnum=14
housekeeping()
while loopnum>0:
    detailloop()
endofjob()
