#arthemetic opertor

a=10
b=3

print("Addition",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:", a/b)
print("floor division:", a// b)
print("remainder:", a % b)
print("power:", a ** b)

#simple calculator
a=int(input("Enter first number: "))
b=int(input("Enter second number:"))

print("addition:", a+b)
print("subtraction:", a-b)
print("multiplication:", a*b)
print("division:",a/b)
print("floor division:",a //b)
print("remainder:", a % b )
print("power:", a ** b)


#student marks calculator
name=int(input("Enter student marks:"))


m1=int(input("Enter python marks:"))
m2=int(int("Enter java marks:"))
m3=int(input("Enter sql marks:"))

total = m1 +m2 + m3
average = total / 3


print("/n____ student report ___")
print("name:",name)
print("total:", total)

#shopping bill calculator
price1 =float(input("enter product 1 price :"))
price2 = float(input("enter product 2 price :"))
price3 = float(input("enter product 3 price :"))
total=price1+ price2+ price3


discount = total *0.10
final_amount =total - discount




print("discount:" , discount)


#assignment operators
x=10


x += 5
print(x)


x-= 2
print(x)
x *= 3
print(x)

#bank balance
balance = 10000


deposit =5000
balance += deposit

print("after deposit:", balance)

withdraw = 2000
balance -= withdraw


print("after withdraw:", balance)


#comparison operates
a =10
b=20


print(a ==b)
print(a !=b)
print(a >b)
print(a < b)
print(a >= b)
print(a <= b)


#age eligibility checker
age = int(input("enter your age:"))


print("eligible:", age >=18)

#pass or fail checker
marks =int(input("enter marks:" ))


print("passed:", marks >=40)

#login validation
correct_username ="admin"
correct_password ="1234"
 

usename = input("enter username")
password = input("enter password:")


print(username == correct_username)
print(username == correct _password)