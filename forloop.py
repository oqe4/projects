words=input("sentence").split("")
pig=""
for word in words:
    pig+=(word[1:]+word[0]+"ay ")
print(pig)
