# PARSING STRING
data="From charanahu605@gmail.com Tue 10 March"
print(data[1,6])
print(data.find("@"))
print(data.find(" ",data.find("@")))
for i in data:
    print(data[data.find("@"),data.find("m")])

