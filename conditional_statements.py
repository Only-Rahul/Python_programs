# program of if , else & elif
age = int(input("enter age : "))
if age <= 13:
    print("child")
elif age <= 18:
    print("teenager")
elif age <= 30:
    print("adult")
else :
    print("senior")


# print grades of students
Marks = float(input("Enter Marks : "))
if Marks >= 80:
    Grade="A"
elif Marks >=60:
    Grade="B"
elif Marks >=40:
    Grade="C"
else :
    print("Fail")

# print house(team) name
House = str(input("Enter condition  :"))
if House == "Good":
    print("Yello")
elif  House == "Average":
      print("Red")
elif House == "below average":
    print("green")
else :
    print("Black")