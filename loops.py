# for variable in iterables:
# block of for Loop

# for x in range(5):
#  print(x)

# for x in range(10,101):
#     print(x)

# for x in range(10,101,4):
#     print(x)

# for x in range(-22,-10):
#    print(x)

# range(start,stop,step)

# for x in range(1,100,2):
#     print(x)


# for x in range(1,100,):
#     print(x)


# print("*")
# print("*",end="")
# print("*")
# print("*",end="")
# print("*",end="")
# print("*")
# print("*",end="")
# print("*",end="")
# print("*",end="")
# print("*")
# print("*",end="")
# print("*",end="")
# print("*",end="")
# print("*",end="")
# print("*")


# for x in range(1,6):
#     for y in range(1,x+1):
#         print('*',end="")
#     print("")

# for x in range(5,0,-1):
#     for y in range(1,x+1):
#         print('*',end="")
#     print("")

# i=1
# while i<=10:
#     print(i)
#     i+=1
# else:
#     print("End of While Loop")

# n = int(input("Enter the numbers:"))
# sum = 0
# while n > 0:
#     r = n % 10
#     sum += r
#     n //=10
# else:
#     print("Sum is",sum)


# n = 446
# sum = 0
# Loop 1 (n > 0) True
# r = n % 10  # r = 446 % 10 = 6
# sum += r  # sum = sum + 6 = 0 + 6 = 6 (sum = 6)
# n //= 10  # n = n // 10 = 446 // 10 = 44 (n = 44)

# Loop 2 (n > 0) (44 > 0 => True)
# r = n % 10  # r = 44 % 10 = 4
# sum += r  # sum = sum + r (sum = 6 + 4 = 10) (sum = 10)
# n //= 10  # n = n // 10 = 44 // 10 = 4 (n = 4)

# Loop 3 (n > 0) (4 > 0 => True)
# r = n % 10  # r = n % 10 = 4 % 10 = 4
# sum += r  # sum = sum + r (sum = 10 + 4 = 14) (sum = 14)
# n //= 10  # n = n // 10 = 4 // 10 = 0 (n = 0)

# Loop 4 (n > 0) (0 > 0 => False)

# Jump Statements - pass , break(terminate a loop) , continue(skips an iteration)

for x in range(5):
    pass
print("hdsj")

for x in range(5):
    if(x==3):
        break
    print(x)
print("out of the loop")


for x in range(5):
    if(x==3):
        continue
    print(x)
print("out of the loop")