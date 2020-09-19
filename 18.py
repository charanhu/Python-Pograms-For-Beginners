#write a program which repitedly repeats number until user enter done.
#once done is enter printout the total , count, average of number.
#if user enters any thing other than a number detect ther mistake print an eror message
#and skip to nextnumber
count=0
total=0
avg=0
while True:
    x=input("enter the input=")
    if(x=="done"):
        break
    else:
        print(x)
        y=int(x)
        count=count+1
        total=total+y
        avg=total/count
    
print("total=",total)
print("count=",count)
print("average=",avg)
        
