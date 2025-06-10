# convert string into int
my_string="256482"
int_num=int(my_string)
print("1  ",int_num)
# convert int into float
int_num=5864
float_num =float(int_num)
print("2  ",float_num)
# convert list into string
my_list=[2,8,5]
my_str =tuple(my_list)
print("3  ",my_list)
# convert list to set 
my_list2=[2,5,7,8,9,6,5]
my_set=set(my_list2)
print("4  ",my_set)
# convert set into dictonary
my_set={2,5,7,8,9,6,5}
my_dic=list(my_set)
print("5  ",my_dic)
# convert str into bool
my_str="google"
my_bool = bool(my_str)
print("6  ",my_bool)
# add two numbers 
my_num=int(input("enter the number"))
my_num2=int(input("enter the number"))
sum=bin(my_num*my_num2**53)
print("**53 :",sum)
no=0b1001000010011010010001101001011101100101111101010011000010010000110100111000110101011010011100100011000100000111001110100000001101000011001111001100001100111101111101110001
cot=int(no)
print(cot)
