print("1.Calculate average of 5 numbers.")
print("Enter 5 numbers : ")
sum = int(input()) + int(input()) + int(input()) + int(input()) + int(input())
print("Average of this five numbers is",sum/5)
print("--------------------------------------------------------------------")
print("2.Check whether number is even or odd.")
a = int(input("Enter a number "))
if a%2 == 0:
    print(a," is even")
else:
    print(a," is odd")
print("--------------------------------------------------------------------")
print("3.Take a year and check whether it is leap year or not")
year = int(input("Enter a year "))
if year%4 == 0:
    print(year," is leap year")
else:
    print(year,"It is not a leap year")
print("--------------------------------------------------------------------")
print("4.Take a number and check whether it is zero, positive or negative.")
a = int(input("Enter a number "))
if a==0:
    print("Number is zero")
elif a>0:
    print("Number is positive")
else:
    print("Number is Negative")
print("--------------------------------------------------------------------")
print("5.Take 2 numbers and display greatest number. (Also check equal number condition)")
a,b = int(input()),int(input())
if a>b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is lesser than b")
print("--------------------------------------------------------------------")
print("6.Take a number and find factorial of that number.")

def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1)*n

n = int(input("Enter a number "))
print("Factorial of this number is ",fact(n))
print("--------------------------------------------------------------------")
print("7.Write a program to swap 2 numbers using third variable.")
a,b = int(input("Enter two numbers")),int(input())
print("Before swaping a is",a,"b is",b)
temp = a
a = b
b = temp
print("After swaping a is",a,"b is",b)
print("--------------------------------------------------------------------")
print("8.Take 2 numbers and find smallest number.")
a,b = int(input("Enter number ")),int(input("Enter second number"))
if a<b :
    print(a," is smallest")
elif a == b:
    print("Both are equal")
else:
    print(b," is smallest")
print("--------------------------------------------------------------------")
print("9.Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.")
a = int(input("Enter a number :"))
if a<100:
    print(a,"is less than 100")
    if a%2 == 0:
        print(a,"is even")
    else:
        print(a,"is odd")
else:
    print(a," is not less than 100")
print("--------------------------------------------------------------------")
print("10.Take a number to print the square of a number if it is less than 10.")
a= int(input("Enter a number "))
if a<10:
    print(a,"is less than 10")
    print("It's square is",a*a)
else:
    print("It is not less than 10")
print("--------------------------------------------------------------------")
print("11.Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .")
a = int(input("Enter a number "))
if a==0:
    print("Number is zero")
else:
    if a>0:
        print("Number is positive")
    else:
        print("Number is Negative")
print("--------------------------------------------------------------------")
print("12.Take 3 numbers and find greatest number using nested IF….ELSE statement.")
a,b,c = int(input("Enter three numbers ")),int(input()),int(input())
if a>b:
    if a>c:
        print(a,"is greatest")
    else:
        print(c,"is greatest")
else:
    if b>c:
        print(b,"is greatest")
    else:
        print("c is greatest")
print("--------------------------------------------------------------------")
print("13.Take 3 numbers and find greatest number using logical operator.")
a,b,c = int(input("Enter three numbers: ")),int(input()),int(input())
if a>b and a>c:
    print(a," is greatest")
elif b>c and b>a:
    print(b," is greatest")
else:
    print(c," is greatest")
print("--------------------------------------------------------------------")
print("14.Write a program to swap 2 numbers without taking third variable.")
a,b = int(input("Enter two numbers: ")),int(input())
print("Before swaping a is",a,"b is",b)
a=a+b
b=a-b
a=a-b
print("After swaping a is",a,"b is",b)
print("--------------------------------------------------------------------")
print("15.Take starting number and ending number from the user and print following series.")
print("30 27 24 21 18 15 12 9 6 3 0")
a,b = int(input("Enter starting number: ")),int(input("Enter ending number: "))
list1 = []
for i in range(b, a+1, 3):
    list1.append(i)
list2 = sorted(list1, reverse=True)
for x in list2:
    print(x)
