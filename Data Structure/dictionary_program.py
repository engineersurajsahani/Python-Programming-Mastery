# Dictionary :- 

# (1) It store data in key value pairs 
# (2) Key must be unique 
# (3) Values can be duplicate

d=dict()
print(d)

d[1]=66
d[2]=77
d[3]=88
d[4]=66
d[6]=33
d[5]=88
d[6]=35

print(d)

print(d.keys())
print(d.values())
print(d.items())

for key in d.keys():
    print("Key :- ",key," Value :- ",d[key])

for value in d.values():
    print("Value :- ",value)

for key,value in d.items():
    print("Key :- ",key," Value :- ",value)

for index,key in enumerate(d):
    print("Index :- ",index," Key :- ",key," Value :- ",d[key])