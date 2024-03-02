# p16 task 1

scnd = ""

n1 = int(input())
scnd = n1

n2 = int(input())
if n2 > n1:
    scnd = n2

n3 = int(input())
if (n3 < scnd) and (n3 > n2) and (n3 > n1):
    scnd = n3

n4 = int(input())
if (n4 < scnd) and (n4 > n2) and (n4 > n1) and (n4 > n3):
    scnd = n4

n5 = int(input())
if (n5 < scnd) and (n5 > n2) and (n5 > n1) and (n5 > n3) and (n5 > n4):
    scnd = n5

n6 = int(input())
if (n6 < scnd) and (n6 > n2) and (n6 > n1) and (n6 > n3) and (n6 > n4) and (n6 > n5):
    scnd = n6

n7 = int(input())
if (n7 < scnd) and (n7 > n2) and (n7 > n1) and (n7 > n3) and (n7 > 4) and (n7 > n5) and (n7 > n6):
    scnd = n7

n8 = int(input())
if (n8 < scnd) and (n8 > n2) and (n8 > n1) and (n8 > n3) and (n8 > 4) and (n8 > n5) and (n8 > n6) and (n8 > n7):
    scnd = n8

n9 = int(input())
if (n9 < scnd) and (n9 > n2) and (n9 > n1) and (n9 > n3) and (n9 > 4) and (n9 > n5) and (n9 > n6) and (n9 > n7) and (n9 > n8):
    scnd = n9

n10 = int(input())
if (n10 < scnd) and (n10 > n2) and (n10 > n1) and (n10 > n3) and (n10 > 4) and (n10 > n5) and (n10 > n6) and (n10 > n7) and (n10 > n8):
    scnd = n10

print("2nd smallest value is:", scnd)