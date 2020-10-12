from numpy import *

n= int (input("Enter a positive odd integer"))
while n%2==0 or n < 1:
    n = int (input("Enter a positive odd integer"))
a= zeros((n, n), dtype= int)
# print(a)
m= int (n/2)
row= 0
col= m
a[row, col]= 1
count= 2
while count<= n*n:

    if (row-1 >= 0) and (col+1<= n-1) and (a[row-1, col+1]!= 0):    #if existing element
        row+= 1
        a[row, col]= count

    elif (row-1 >= 0) and (col+1<= n-1) and (a[row-1, col+1]== 0):  # fill diagonally
        while row-1 >= 0 and col+1<= n-1 and a[row-1, col+1]== 0:
            col += 1
            row -= 1
            a[row, col]= count
            count+= 1
        count-=1

    elif (row-1< 0) and (col+1> n-1):   #if both row and col out of range
        row+= 1
        a[row, col]= count

    else:
        if (row-1< 0) or (col+1 > n-1):   #if row or col out of range but not both
            if row== 0:
                col+= 1
                if row== 0:
                    row= n-1
                else:
                    row= 0
            elif (col== 0) or (col== n-1):
                row-= 1
                if col== 0:
                    col=n-1
                else:
                    col= 0
            a[row, col]= count

    count+= 1

print(a)

# checking if valid magic square
def check(a):
    colsum= sum(a, axis=0)
    rowsum = sum(a, axis=1)
    diogsum1= 0
    diogsum2= 0
    for i in range(n):
        diogsum1 += a[n- i -1, i]
        diogsum2 += a[i, n - i - 1]
    colset= set(colsum)
    rowset= set(rowsum)
    if (size(colset) == size(rowset) == 1) and diogsum1 == diogsum2 == list(colset):
        print("correct")
check(a)