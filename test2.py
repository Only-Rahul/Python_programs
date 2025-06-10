# write a program to find largest number into two numbers by user input ?
a=int(input("enter number a : "))
b=int(input("enter number a :"))
if a > b :
    print("largest number is ",a)
else:
    print("largest number is ",b)
# write a program to find largest number into three numbers by user input ? 
a=int(input("enter number a :"))
b=int(input("enter number b :"))
c=int(input("enter number c :"))
if a > b and c:
    print("largest number is ",a)
elif b > c and a :
    print("largest number is ",b)
elif c > b and a :
    print("largest number is ",c)
else:
    print("error")
# 3rd
a=int(input("enter number a :"))
b=int(input("enter number b :"))
c=int(input("enter number c :"))
largest= a
if a>b and a>c:
    print("largest number is ",a)
elif b>a and b>c:
    print("largest number is ",b)
else:
    print("largest number is ",c )


# program to find out largest value from list using operators
list1=[10,20,30,40,50]
largest_no=list1[0]
for num in list1:
    if num>largest_no:
        largest_no=num
    print(" print the larger number:",max(list1))

# write a program to get user name and age >=18 (adult)
name=input("enter your name : ")
age=int(input("enter your age : "))
if age>=18:
    print("you are adult")
else:
    print("not valid")

# leap year program
year= int(input("Enter the number"))
if year%4==0:
        print("leap")
else:
        print("not_leap")

# write a program to cosider days of weak as numbers
day = str(input("enter the day : "))
if day == "Monday":
    print("1")
elif day == "Tuesday":
    print("2")
elif day == "Wednesday":
    print("3")
elif day == "Thursday":
    print("4")
elif day == "Friday":
     print("5")
elif day == "saturday":
    print("6")
elif day == "sunday":
    print("7")
else:
    print("invalid text")

# create a calculater ?
num = int(input("enter number"))
operator=input("")
num1=int(input("enter number"))
if operator=="+":
    result=num+num1
elif operator=="-":
    result=num-num1
elif operator=="*":
    result=num*num1
elif operator=="/":
    if num1%2==0:
        print("not zero.")
else :
    result=num/num1
print("Result is : ", result)


# # write a program to print vovels
alp=str(input("enter the character : "))
char = "aeiouAEIOU"
if alp in char:
    print("vovel")
else:
    print("Not vovel")
 
