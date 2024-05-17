#payten
#2/9/2024
#idek
year=int (input("Please enter the year? (NNNN) : "))
#example of clear prompt
yearcheck=input (str(year)+ ": is that right? (y/n): ")
#example of echoing input
month=11
day=8 #example of good variable name
hour=12
minute=19
second=30

#use \ for dividing lines to be more readable
if 1900 < year < 2100 and 1 <= month <= 12 and 1 <= day <= 31 \
   and 0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60: #looks like a valid date
    print(True)
    
    
