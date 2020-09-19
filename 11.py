a=int(input("enter a= "))
b=int(input("enter b= "))
print("1.add 2.sub 3.mul 4.div\n")
print("enter the choice= ")
c=int(input())
if (c==1):
    add=a+b
    print(add)
elif (c==2):
    sub=a-b
    print(sub)
elif (c==3):
    mul=a*b
    print(mul)
elif (c==4):
    div=a/b
    print(div)
else:
    print("error")