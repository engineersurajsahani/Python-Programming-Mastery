# Factorial 5! = 1*2*3*4*5 

n=5
result=1

for i in range(1,n+1):
    result=result*i

print("Factorial of ",n," is ",result)

# Fibonacci Series 1 1 2 3 5 8 ...
    
print("\n\n1 1 ",end=" ")

firstNumber=1
secondNumber=1 

for i in range(3,11):
    thirdNumber=firstNumber+secondNumber
    print(thirdNumber,end=" ")
    firstNumber=secondNumber
    secondNumber=thirdNumber


