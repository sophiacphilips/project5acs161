#Author: Sophia Philips
#Github Username: sophiacphilips
#Date:10/25/22
#This code take two integers and multiplies them using addition via recursion rather than directly multiplying them together.

def mult(a,b):
#account for input of 0
    if a==0:
        return 0
    return mult(a-1,b) + b
#test
a=int(input())
b=int(input())
print(mult(a,b))


