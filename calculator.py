# calculator
a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
print("Airthmatic operator","sub",a-b,"add",a+b,"mal",a*b,"div",a/b)
print("comperision operator","gt",a<b,"lt",a>b,"gtet",a<=b,"ltet",a>=b,"et",a==b,"ne",a!=b)
print("logical operator","and",(a<b)and(b>a),"or",(a<b)or(b>a),"not",not(a<b))
x=5
x+=5
print("assingment operator",x)
print("bitwiser",a&b,b|a,~b)
print("identity operator",x is not 5)
print(x is 5)
a=int(input("Enter the number : "))
condition=(input("enter the condition"))
b=int(input("Enter the number : "))

# if condit
# arithmatic operator using conditional statement
if condition == "+": 
    print("addition",a+b)
elif condition == "-": 
    print("sub",a-b)
elif condition == "*": 
    print("mal",a*b)
elif condition == "/": 
    print("div",a/b)
else:
    print("wrong input")
# comperision operator
if a<b:
    print("greater than",a>b)
elif a>b:
    print("smaller than",a<b)
else:
    print("error")
# logical operator
if (a<b)and(b<a):
    print("and",(a<b)and(b<a))
elif (a<b)or(b>a):
    print("or",(a<b)or(b>a))
else:
    print("not",not(a<b))
# assignment operator
if condition == "+=":
    print("assingment operator,a+=",b)
elif condition == "-=":
    print("assingment operator,a-=",b)
elif condition == "*=":
    print("assingment operator,a*=",b)
elif condition=="a/=b":
    print("asingment oprator,a/=",b)
else:
    print("wrong input")