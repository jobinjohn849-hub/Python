'''
  tuple is a collection of heterogenous data.
  - Ordered
  - Indexed
  - Allow duplicates
  - iMmutable

'''

t1 = (1,2,3,4,5)
print(t1)
print(type(t1))
t2 = 45, 56, 79, 72 #packing
print(t2)
print(type(t2))
a,b,c=(1,2,3)#unpacking

for x in t1:
    print(x)
print(len(t1))
print(1 in t1)
print(t1[0])
print(t1[:-2])
print(t1[2:])
print(t1[::2])
print(t1[::3])
