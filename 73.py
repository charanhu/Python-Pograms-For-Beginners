f = open("demofile.txt")
string=f.read()
# Splits at space
list=string.split()
print(list)
print("-----------------------")
list1=list.sort()
print(list1)