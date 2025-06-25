# List :- 

# (1) It is like a container in which we can store multiple data.
# (2) Data can be of the same type or different type.
# (3) We can also store duplicate elements.
# (4) It is changeable
# (5) It maintain insertion order.

l=list()

l.append(10)
l.append(30)
l.append(20)
l.append(10)
l.append(30)
l.append(20)

l.append(7.7)
l.append('c')
l.append('Hello')
l.append(True)
l.append(False)

print(l)

l[6]=88
print(l)

l.pop()
print(l)

l.pop(3)
print(l)

l.remove('c')
print(l)

l.remove('Hello')
print(l)

del l[6]
print(l)


l.append(1)
l.append(100)
l.append(50)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

print("Max :- ",max(l))
print("Min :- ",min(l))