#counting startswith in a file
count=0
fp=open('text.txt','r')
for i in fp:
    if(i.startswith("python")):
        count=count+1
print(count)





