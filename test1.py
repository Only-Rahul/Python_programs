
num=int(input("enter the number  :"))
num2=int(input("enter the number  :"))
sum=num+num2
sub=num-num2
mul=num*num2
dev=num/num2
mod=num%num2
print("addition result  :",sum)
print("substraction result  :",sub)
print("multiplication result  :",mul)
print("devision result  :",dev)
print("modulas result  :",mod)
# add two 
list=[1,58,"j&k","punjab"]
list1=[1,78,"pen","gun"]
print(list)
print(list1)
# add list and list1
combine=list.__add__([1,78,"pen","gun"])
print(combine)
# dictonary 
dict={"obj":"pen","obj1":"pencile","obj2":"notebook"}
del dict["obj"]
print(dict)
# find the area of rectangle
length=int(input("enter the length of rectangle  :  "))
breath=int(input("enter the breath of rectangle  :  "))
area=length*breath
print("area of rectangle is  :",area)
# find the area of square
s1=int(input("enter the length of a side  :   "))
area=s1*s1
print("area of square",area)
# find the radius of circle
import math
r=int(input("enter the radius of circle  :  "))
area=math.pi*r*r
print("area of circle is  :",area)