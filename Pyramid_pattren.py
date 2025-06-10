# Pyramid pattren 
# outer loop
from builtins import range
from builtins import print
# lefthalf pyramid
Row = 9
for i in range(1,Row+1):
    for j in range(i):
        print("*",end="")
    print()


# Righthalf pyramid
Row = 9
for i in range(1,Row+1):
    for j in range(Row-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()

# Full pyramid loop ?
Row = 5
for i in range(1,Row+1):
    for j in range(Row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

# inverted
row = 9
for i in range(row,0,-1):
    for j in range(0,row-1):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()

# left
for i in range(1,row+1):
    for j in range(i):
        print("*",end="")
    print()
# right
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
# full
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    print()
# inverted right
for i in range(row,0,-1):
    for j in range(0,row-1):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
# invered left
for i in range(row,0,-1):
    for j in range(0,row-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()

# inverted full
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
row=18
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

row = 8
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print() 
