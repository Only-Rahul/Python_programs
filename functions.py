# # user define functions
# def greet():# declier function without perameter and without return type
#     print("good morning")
# greet()
# def add(a,b):# declier perameters a and b and without return type
#     print(a+b)
# add(2,2)# put  arguments 2 , 2
# def add(a,b):#function with return type
#     return (a+b)
# num = add(4,4)
# print(num) 
# def sq(a):
#     return a*a
# num = sq(5)
# print(num)
# def find_even():
#     even_numbers = ()
#     for i in range(1,14):
#         if i % 2 == 0:
#             print("Even.No :",i)
# find_even()
# find the three largest number by user define function
# def find_largest_values():
#     num =(input("Enter the value : "))
#     num1 =(input("Enter the value : "))
#     num2 =(input("Enter the value : "))
#     num3 =(input("Enter the value : "))
#     num4 =(input("Enter the value : "))
    
#     if num < num1 and num2 and num3 and num4 :
#         print(num)
#     elif num1 < num and num2 and num3 and num4:
#         print(num1)
#     elif num2 < num1 and num and num3 and num4:
#         print(num2)
#     elif num3 < num1 and num2 and num and num4:
#         print(num3)
#     elif num4 < num1 and num2 and num3 and num:
#         print(num4)
#     for i  in num , num1 , num2 , num3 , num4 :
        
#         print(i)
# find_largest_values()

# def largest_number(num,num1):
#     if num<num1:
#         return num1
        
#     else:
#         return num
# print(largest_number(2,8))

# def find_three_highest():
#     """
#     Prompts the user to enter numbers and then prints the three highest values.
#     """
#     numbers = []
#     while True:
#         user_input = input("Enter a number (or type 'done' to finish): ")
#         if user_input.lower() == 'done':
#             break
#         try:
#             number = float(user_input)
#             numbers.append(number)
#         except ValueError:
#             print("Invalid input. Please enter a number or 'done'.")

#     if len(numbers) < 3:
#         print("Please enter at least three numbers to find the three highest.")
#     else:
#         # Sort the list in descending order
#         numbers.sort(reverse=True)
#         print("The three highest values are:", numbers[0], numbers[1], numbers[2])
# find_three_highest()

# # Call the function to execute the program
# find_three_highest()

# def find_highest_value():
#     numbers=[]
#     while True:
#         user = input("enter the value : ")
#         if user.lower() == 'done':
#             break
#         try:
#             number = float(user)
#             numbers.append(number)
#         except valueerror:
#             print("invalid input")
#     if len(numbers)<3:
#         print("enter alleast 3 values !")
#     else:
#         print("these are top three values ",numbers[0],numbers[1],numbers[2])
# find_highest_value()

# display table
# def 
# ########
# def greet():
#     for i in range(0,8):
#         print("good Morning")
# greet()

# def largest():
#     list=[1,5,6,8,4,9,2,7]
#     print(max(list))
# largest()

# def length():
#     word = "Jokar"
#     print(len(word))
# length()

# def check(num):
#     if num > 0:
#         print("positive")
#     else:
#         print("negtive")
# check(-66)

# def even():
#     for i in range(0,13):
#         if i % 2 == 0:
#             print(i)
# even()

# def swap(a,b):
#     print("a=",a,"b=",b)
#     a,b=b,a
#     print("a=",a,"b=",b)
# swap(3,7)


# def add(a,b):# declier perameters a and b and without return type
#     print(a+b)
# add(2,2)# put  arguments 2 , 2

# def add(a,b):#function with return type
#     return(a+b)
# num = add(4,4)
# print(num)


# def sq(a):
#     return a*a
# num = sq(5)
# print(num)


# # find the vovals from a to z
# def find():
#     for i in range(65,91):
#         print(chr(i),end="  ")
#     for j in range(97,123):
#         print(chr(j),end=" ")
# find()

