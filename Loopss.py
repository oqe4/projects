number=1 #1
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

def power(base, exponent): #2

    total = 1
    while exponent > 0:
        total = total * base
        exponent = exponent - 1
    return total

def factorial(n):

    r=1
    while n > 0:
        r=r*n
        n=n-1
    return r

print(factorial(3))
print(power(3, 4))

count=0 #3
while True:
    count+=1
    if count > 10:
        break
    if count == 5:
        continue
    print (count)

i=1 #4

while(i<=10):
    print("6*",i,"=",6*i)

    if i >= 5:
        break

    i=i+1

for i in range(25):
    if i == 3:
        continue
    print(i)

myvar="" #5
global loopnum, name, file

loopnum=14
housekeeping()
while loopnum>0:
    detailloop()
endofjob()



