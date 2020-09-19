def chop(list):
    print(list)
    for i in range(0,len(list)):
        list.remove(list[0])
        print(list)
        list.remove(list[(len(list))-1])
        print(list)
       
# creating an empty list 
lst = [] 

# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
print("Enter the list values")
# iterating till the range 
for i in range(0, n): 
    ele = input()
    lst.append(ele) # adding the element 

chop(lst)