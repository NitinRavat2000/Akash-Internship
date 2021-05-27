#Day 2 Basic Task in Internship
print("Hello World")

a,b = "is in GEC ", "Gandhinagar, sector"
c = 28
print("Nitin "+a+b,c)
print(type(a),type(b),type(c))
'''Type of
            Variable'''
a = 1 + 2j
print("a =", a, "is of ", type(a))
print("Is \"a\" Complex number ? ",isinstance(a, complex))
#String
name = "Nitin Ravat "
print(name[5])       # letter printing
print(name[:7])      # Start (By Default) : END
print(name[8:])      # Start : END (By Default)
print(name[3:10])    # Start : END
print(name * 2)

#LIST Datatype
print("")
print("List DataType")
print("")
list = [10, 5.5 ,"Kotyark", 10, "Store", 10]
print(list)
print(list[2],"This variable \"list\" is of type",type(list))
print(list[1:3], list[2:], list[:2])
list.append("Rajkot")
print(list)
print("\"10\" is available in list ", list.count(10), "times")

print("")
print("Tuple Oprations")
print("")
#Tuple
print("Tuple DataType")
tuple = (10, 5.5 ,"Kotyark","Store")
print(tuple)
print(tuple[2],"This variable \"tuple\" is of type",type(tuple))
print(tuple[1:3], tuple[2:], tuple[:2])

print("")
print("Dictionary Data Type")
print("")
dict = {1:"15", 2:"Days", 3:"Internship" ,"ak":'in', 5:"Akash Technolabs"
       , 6:[1,2,3,4,5]}
print(dict)
print(dict.keys())
print(dict.values())
print(dict["ak"])
print("list in Dictionary",dict[6])