# Tuple :- 

# (1) It is like a container in which we can store multiple data.
# (2) Data can be of the same type or different type.
# (3) We can also store duplicate elements.
# (4) It is not changeable
# (5) It maintain insertion order.

t=tuple([1,2,3,4,5,6,3,4,"Hello"])
print(t)

t=list(t)

t.append(100)

t=tuple(t)

print(t)