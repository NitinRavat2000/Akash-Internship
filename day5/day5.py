print("Problem :1")


class cal1:
    x = 0
    y = 0
    z = 0

    def setdata(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c

    def display(self):
        print(self.x + self.y + self.z)


pro1 = cal1()
pro1.setdata(2, 4, 6)
pro1.display()
print("------------------------------------------------------")
print("Problem :2")


class cal2:
    r = 0
    area = 0

    def setdata(self):
        self.r = int(input("Enter radius of circle : "))

    def area(self):
        self.area = 3.14 * self.r * self.r

    def display(self):
        print("Area of this circle is", self.area)


pro2 = cal2()
pro2.setdata()
pro2.area()
pro2.display()
print("------------------------------------------------------")

print("Problem :3")


class cal3:
    p = r = n = 0
    intrest = 0

    def __init__(self, p, r, n):
        self.p = p
        self.r = r
        self.n = n

    def calintrest(self):
        self.intrest = (self.p * self.r * self.n) / 100

    def display(self):
        print("Intrest for given values is : ", self.intrest)


p = int(input("Enter amount : "))
r = int(input("Enter rate per annum : "))
n = int(input("Enter number of duration in years : "))
pro3 = cal3(p, r, n)
pro3.calintrest()
pro3.display()

print("------------------------------------------------------")
print("Problem : 4")


class cal4:
    def setdata(self, n):
        self.n = n

    def display(self):
        self.sqre = pow(self.n, 2)
        return self.sqre


pro4 = cal4()
pro4.setdata(int(input("Enter number : ")))
print("Square of this number is", pro4.display())
print("------------------------------------------------------")
print("Problem : 5")


class employee:
    name = "Nitin"
    designation = "Business Analyst"

    def __init__(self):
        print("Employee class [ name :", self.name, ", designation :", self.designation, "]")


class personal(employee):
    salary = 100000

    def __init__(self):
        print("Employee class [[ name :", self.name, ", designation :", self.designation, "] sub class [ salary :",
              self.salary, "]]")


pro5 = personal()
print("------------------------------------------------------")
print("Problem : 6")


class cal5:
    l = w = 0
    area = 0

    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calarea(self):
        self.area = self.l * self.w

    def display(self):
        print("Area of the rectangle is : ", self.area)


l = int(input("Enter length : "))
w = int(input("Enter width : "))
pro5 = cal5(l, w)
pro5.calarea()
pro5.display()
print("------------------------------------------------------")
print("Problem : 7")


class cal6:
    l = 0
    area = 0

    def setdata(self):
        self.l = int(input("Enter length of square :"))

    def area(self):
        self.area = pow(self.l, 2)

    def display(self):
        print("Area of the Square is ", self.area)


pro7 = cal6()
pro7.setdata()
pro7.area()
pro7.display()
print("------------------------------------------------------")
print("Problem : 8")


class publisher:
    title = ""

    def __init__(self):
        print("Publisher class ")

    def gettitle(self):
        self.title = input("Enter Book title :")

    def printtitle(self):
        print("Title of the book is", self.title)


class book(publisher):
    page_no = 0

    def __init__(self):
        super().__init__()
        print("Book class inherits publisher ")

    def getpageno(self):
        self.page_no = int(input("Enter page no of book :"))

    def printpageno(self):
        print("pages of the book is", self.page_no)


class tape(publisher):
    time_for_playing = 0

    def __init__(self):
        super().__init__()
        print("Tape class inherits publisher ")

    def gettime(self):
        self.time_for_playing = int(input("Enter tape playing time :"))

    def printtime(self):
        print("Tape playing time is", self.time_for_playing)


print("Functionalities of BOOK class")
pro81 = book()
pro81.getpageno()
pro81.printpageno()
pro81.gettitle()
pro81.printtitle()
print("")
print("Functionalities of TAPE class")
pro82 = tape()
pro82.gettime()
pro82.printtime()
pro82.gettitle()
pro82.printtitle()
print("------------------------------------------------------")
print("Problem : 9")


class Scheme:
    scheme_id = ""
    scheme_name = ""
    outgoing_rate = 0
    message_charge = 0

    def __init__(self):
        print("Scheme class constructor")

    def getScheme(self):
        self.scheme_id = input("Enter scheme id :")
        self.scheme_name = input("Enter scheme name :")
        self.outgoing_rate = int(input("Enter outgoing rate :"))
        self.message_charge = int(input("Enter message charge :"))

    def printScheme(self):
        print("Printing Scheme details...")
        print("Scheme id of the Scheme is", self.scheme_id)
        print("Scheme name of the Scheme is", self.scheme_name)
        print("Outgoing rate of the Scheme is", self.outgoing_rate)
        print("Message charge of the Scheme is", self.message_charge)


class customer(Scheme):
    cust_id = ""
    name = ""
    mobile_no = 0

    def __init__(self):
        super().__init__()
        print("Customer class constructor ")

    def getcust(self):
        self.cust_id = input("Enter customer id :")
        self.name = input("Enter your name :")
        self.mobile_no = int(input("Enter your mobile no :"))

    def printcust(self):
        print("Printing customer details...")
        print("Customer id :", self.cust_id)
        print("Name :", self.name)
        print("Mobile no :", self.mobile_no)


print("Functionalities of Customer class")
pro91 = customer()
pro91.getcust()
pro91.printcust()
pro91.getScheme()
pro91.printScheme()
print("------------------------------------------------------")
print("Problem : 10")


class arith:
    a = b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
pro10 = arith(a, b)
print("Addition :", pro10.add())
print("Substraction :", pro10.sub())
print("Multiplication :", pro10.mul())