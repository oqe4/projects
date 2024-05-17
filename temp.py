def convert_temp(temp):
    temp=temp*9
    temp=temp/5
    temp=temp+32
    return temp

temp = convert_temp(temp)
print(temp)
