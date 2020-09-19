#default reads the file
count=0
f = open("calculator1.txt")
for i in f:
    count=count+1
    print(i)
print(count)