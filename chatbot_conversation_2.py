import random
from time import sleep

def bot1(response):
    global yeahcount
    if ("sing" in response.lower()):
        response= "mock"
    elif ("yeah" in response.lower()):
        if yeahcount==0:
            response="ing"
            yeahcount+=1
        elif yeahcount==1:
            response="bird"
            yeahcount+=1
        else:
            response="yeah"

    else:
        response=random.choice(["yeah"])
    return response
        
def bot2(response):
    if ("mock" in response.lower() or "ing" in response.lower() or "bird" in response.lower()):
        response= "yeah"
    
    else:
        response=random.choice(["yeah"])
    return response
        
global yeahcount
yeahcount=0
response=input("What do you want the first bot to say?")
while True: #infinite loop
    response = bot1(response)  #f(X)
    print (response)
    sleep(2)
    response = bot2(response)
    
    print (response)
    sleep(2)











    
    
