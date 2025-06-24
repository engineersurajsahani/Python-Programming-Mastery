# Function without parameter and without return statement

def hello():
    print("Hello")

hello()

# Function with parameter and without return statement

def add(a,b):
    print("Addition of a and b :- ",a+b)

add(4,5)
add(7,5)

# Function without parameter and with return statement

def data():
    return 55

a=data()
print("Value of a :- ",a)

# Function with parameter and with return statement

def sum(a,b,c):
    return a+b+c

result=sum(4,5,6)
print("Result :- ",result)

result=sum(10,20,30)
print("Result :- ",result)