""""
Session - 01
Date - 16/12/2023
Note: SumOfDigits and Difference between sumOfDigits of left and right numbers in a decimal number.

Task:
    1. Java - hold
    2. understand today's program
    topics - functional programming, string inbuilt methods python
"""

# 666.888 -> 18 - 24 = -6
#3.14 -> 3 - 5 = -2
#90.10 -> 9 - 1 = 8

"""
function splitNumber(number):
    // Your logic
    return leftNumber, rightNumber
    
function sumOfDigits(number):
    // Your logic
    return digitSum

step 1 - userInput = input()
step 2 - left, right = splitNumber(userInput)
step 3.1 - leftSum = sumOfDigits(left)
step 3.2 -rightSum = sumOfDigits(right)
step 4 - print(leftSum - rightSum) 

"""

def sumOfDigits(number):
    var=int(number)
    sum=0
    while var!=0:
        result=var%10
        sum=sum+result
        var=var//10
    return sum

def splitNumber(number):
    inputNumber = str(number)
    splitInput = inputNumber.split(".")
    left = splitInput[0]
    right = splitInput[1]
    return left, right

# Main Code Here
number=input()
left,right=splitNumber(number)
leftSum=sumOfDigits(left)
rightSum=sumOfDigits(right)
print(leftSum-rightSum)
