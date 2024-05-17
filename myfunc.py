x = "awesome"

def myfunc1():
    print("Python is " + x)

    myfunc1()

    ###################################

    y = "awnsome"

    def myfunc2():
        y = "fantastic"
        print("Python is " + y)



    myfunc2()

    print("Python is " + y)

    ####################################

    def myfunc3():
        global z
        z = "fantastic"

    myfunc3()

    print("Python is " + z)

