# Reverse Number 1234 ---> 4321 

n=1234 
a=n
sum=0

while n != 0:
    rem = n % 10 # rem = 1 % 10 = 1
    sum = sum * 10 + rem # sum = 432 * 10 + 1 = 4321
    n= int(n / 10) # n = 1 / 10 = 0

print("Reverse of ",a," is ",sum)