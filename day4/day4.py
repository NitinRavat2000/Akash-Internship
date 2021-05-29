#Day 4 in internship in python Django
def myFunction():
    name = "Nitin Ravat"
    contact = 9998930378
    return(name,contact)

name,contact = myFunction()
print(name,contact)

print("")
print("default arguments")
def ifidonotpass(a=23,b=28):
    print(a+b)

ifidonotpass(10,20)
print("")
print("Parameter not passed")
ifidonotpass()

print("")
print("keywordargument")
ifidonotpass(b=30,a=45)


print("variable length arguments")
print("Non keyworded")
def sumofmarks(*argu):
    sum=0
    for i in argu:
        sum = sum + i
    return sum

print(sumofmarks(10,20,30,40,50))
print("")
print("Keyworded")
def myFun(**arg):
    for i,j in arg.items():
        print(i,j)

myFun(Name="Dhairya" , Surname="Shaherawala")

print("")
def fun():
    x=100
    print("x inside the function : ",x)

x=215
fun()
print("x outside the function : ",x)

print("Arithmetic operaters")
x=10
y=20
print("y+x",y+x)
print("y-x",y-x)
print("y*x",y*x)
print("y/x",y/x)
print("y//x",y//x)
print("y**x",y**x)

print("")
print("Relational operaters")
x=10
y=20
print("y>x is",y>x)
print("y<x is",y<x)
print("y<=x is",y<=x)
print("y>=x is",y>=x)
print("y==x is",y==x)
print("y!=x is",y!=x)

print("")
print("Logical operaters")
a,b,c = int(input("Enter three numbers: ")),int(input()),int(input())
if a>b and a>c:
    print(a," is greatest")
elif b>c and b>a:
    print(b," is greatest")
else:
    print(c," is greatest")

print("")
print("Membership operaters")
list = [1,3,5,7,9]
print(list)
print("2 in list",2 in list)
print("5 in list",5 in list)

print("")
print("Indentity operaters")
x = 200
y = 200
print("x is",x,"y is",y)
print("x is y : ",x is y)
print("x is not y",x is not y)