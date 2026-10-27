'''
  list is a collection of heterogenous data.
  - Ordered
  - Indexed
  - Allow duplicates
  - Mutable

'''

# numbers = [78,96,77,36,10,2,75,34]
# print(numbers)
# print(type(numbers))
# print(len(numbers))
# print(numbers[6])
# print(numbers[-1])
# print(numbers[1:6])
# print(numbers[-7:-2])
# print(numbers[:-2])
# print(numbers[4:])
# print(numbers[::2])
# print(numbers[::-1])
# print(numbers[::-2])
# print(numbers[::-3])
# print(numbers[0])
# numbers[4]=100
# numbers.append(867)
# numbers.append(8)
# numbers.insert(5,23)
# # numbers.extend("wayne")
# numbers.extend([86,77,99])
# print(numbers)

# even_count = 0
# for n in numbers:
#     if n%2 == 0:
#         even_count +=1
# print(even_count)

# l2 = []
# l3 = list(numbers)
# print(numbers)
# print(l3 is numbers)

# print(numbers.count(77))
# print(numbers.index(100))
# print(22 in numbers)
# print(22 not in numbers)

# l4 = numbers.copy()

# l4[1]="Abhijith"
# print(l4)
# print(numbers)
# print(l4 is numbers)
# numbers.sort()
# numbers.sort(reverse=True)
# numbers.reverse()
# print(numbers)

# l5 = [[12,13,14],[78,74,20],[100,200,366]]
# print(l5[1][2])
# l6 = l5.copy() 
# l6[1][2] = 555
# print(l5)
# print(l6)

# for x in l5:
#     for n in x:
#         print(n)

numbers = [78,96,77,36,10,2,75,34]
# squared_numbers = []
# for n in numbers:
#     squared_numbers.append(n*n)
# print(f"squared numbers:{squared_numbers}")

# even_numbers = []
# for n in numbers:
#     if n%2 == 0:
#         even_numbers.append(n)
# print(even_numbers)

squared_numbers_comp = [n*n for n in numbers]
print(squared_numbers_comp)
even_numbers_comp = [n for n in numbers if n%2 == 0]
print(even_numbers_comp)
# [expression for item in iterable if clause]

even_or_odd = ["even" if n%2 == 0 else "odd" for n in numbers]
print(even_or_odd)
