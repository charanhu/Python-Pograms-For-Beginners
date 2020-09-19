#write a python function to find max of 3 no
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))


def greatest_ofthree():
    if a>c:
        if a>b:
            print("a is large")
        else:
            print("b is large")
    elif b>c:
        if b>a:
            print("b is large")
        else:
            print("a is large")
    else:
        print("c is large")
        
        
greatest_ofthree()


