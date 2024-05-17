def cal_hypo(s1,s2):
    import math
    a=s1*s1
    b=s2*s2
    answer=math.sqrt (a+b)
    return answer

side1=input("what is side 1?")
side1=int (side1)
side2=input("what is side 2?")
side2=int (side2)
hypo=cal_hypo(side1,side2)
print(hypo)


