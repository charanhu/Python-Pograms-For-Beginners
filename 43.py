#strings matching
#opening file
#reading a file
count=0
f = open("calculator1.txt","r")
for i in f:
    count=count+1
    print(i)
print(count)