count=0
try:
    fp=open('text.txt','r')
except:
    print("error")
    exit()
count=0
for line in fp:
    if line.startswith("afafa"):
        count=count+1
print(count)