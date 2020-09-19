#write a while loop that starts at the last charater of string and works its way backword to the fist charcter in string, printing each letter as a seaparate line
fruit='banana'
lastindex=(len(fruit)-1)
while lastindex >= 0:
    print(fruit[lastindex])
    lastindex=lastindex-1