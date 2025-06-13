# Even Numbers From 1 To 100 

print("\n ***** Even Numbers ***** \n")

for i in range(1,101):
    if i % 2 == 0 :
        print(i,end=" ")

# Odd Numbers From 1 To 100 

print("\n\n ***** Odd Numbers ***** \n")

for i in range(1,101):
    if i % 2 != 0 :
        print(i,end=" ")

# Prime Numbers From 1 To 100 

print("\n\n ***** Prime Numbers ***** \n")

for i in range(2,101):
    check=0
    for j in range(2,i):
        if i % j == 0 :
            check=1
    if check==1:
        pass 
    else:
        print(i,end=" ")