# Operator :- It is just a symbol or sign by which we can perform some predefined action 
# or task or operation.

# Types of Operator :- 
# (1) Arithmetic Operator ( +,-,*,/,% )
# (2) Assignment Operator ( +=,-=,*=,/=,%= )
# (3) Comparision Operator ( <,<=,>,>=,==,!= )
# (4) Logical Operator ( and , or , not )

a=10 
b=20 

# (1) Arithmetic Operator 

print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(a%b)

# (2) Assignment Operator 

a+=b # a=a+b = 10 + 20 = 30  a=30 b=20
print("a :- ",a," and b :- ",b)

a-=b # a=a-b = 30 - 20 = 10  a=10 b=20
print("a :- ",a," and b :- ",b)

a*=b # a=a*b = 10 * 20 = 200  a=200 b=20
print("a :- ",a," and b :- ",b)

a/=b # a=a/b = 200 / 20 = 10  a=10 b=20 
print("a :- ",a," and b :- ",b)

a%=b # a=a%b = 10 % 20 = 10  a=10 b=20 
print("a :- ",a," and b :- ",b)

# (3) Comparision Operator

print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
print(a==b)
print(a!=b)

# (4) Logical Operator 

print("\n***** Logical Operator *****\n")

print(((a==100) and (b==200)))
print(((a==10) and (b==200)))
print(((a==10) and (b==20)))

print(((a==100) or (b==200)))
print(((a==10) or (b==200)))
print(((a==10) or (b==20)))

print(not ((a==100) or (b==200)))