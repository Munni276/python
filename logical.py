 #logical operators
age=25
citizen=True
print(age >=18 & citizen == true)


age=16
citizen = True
print(age >= 18 and citizen ==true)


has_card = False
has_cash =True


print(has_card or has_cash)

is_logged_in =True
print(not is_logged_in)
#atm eligibility checker
balance = 10000
withdraw =5000


print(withdraw > 0 and withdraw <= balance)

#student scholarship eligibility checker
marks = float (input ( "enter marks ;" ))
attendence = float(input ("Enter attendence:" ))

eligible = marks > = 85 and attendence >=75

print("scholarship Eligible;",)

  #identity operates
  a=None
print(a is None)
print(a is not none)


#bitwise operators
a=5
b=3

print(a & b)
print(a | b)
print(a ^ b)

#electricity city bill calculator
units = int(intput("enter electricity units"))

rate = 6
bill = units * rate
print("electricity bill", bill )

#travel expense calculator 
travel = float(input("travel expense:"))
food = float(input("food expense:"))
hotel = float(input("hotel expense:"))


total = travel +food +hotel
print("total expense:", total)  
#list in python
#list is an ordered and changeable that can store multiple values
marks = [80 , 90 , 75 , 85]

print(marks) 
#add elements to a list
marks =[80,90,75]

marks.append(85)

print(marks) 
#remove element from a list
marks =[80,90,75]

marks.remove(90)
print(marks)

a=[1,2,3]
b=[4,5,6]


a.extend(b)
print(a)

number =[20,20,30,20]

number.remove(20)

print(number)

numbers =[10,20,30,40]

print(numbers.index(30))

number=[40,10,30,20]

print(number)

number.sort(reverse=True)
print(number)


a=[1,2,3]

b =a.copy()
print(b)

numbers =[10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[: :-1]) 
n=10
mul=2
for  i in range(1+,n+1):
print(mul,'x',i,'=', mul*i) 
# count of mu(ultiples of 3
n = int(input("enter n :"))

count =0
for i in range(1,n+1):
   if i % 3 == 0 :
      count = count +i

      print("count" ,count) 
      #print all even numbers from 2 to 50
      i = 2
      while i<= 50:
         i = i+2  