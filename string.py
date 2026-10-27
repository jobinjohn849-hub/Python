name = 'amal'
course = "Python Fullstack"
address = '''
kochi
kerala
india
'''

# print(name)
# print(course)
# print(address)
# print(type(name))
# print(course[0])
# print(course[7])
# print(course[15])
# print(course[-1])
# print(course[-6])
# print(len(course))

# # Slicing[start:end:step]

# print(course[0:5])
# print(course[-10:-5])
# print(course[:6])
# print(course[6:])
# print(course[2:10:2])
# print(course[::2])
# print(course[::-1])

# for x in course:
#     print(x)


# print(course.upper())
# print(course.lower())
# print(course.capitalize())
# print(course.title())
# print(course.swapcase())
# print(course.isupper())
# print(course.islower())

# print(course.index('Fullstack'))
# print(course.count('l'))
# print('6383'.isdigit())
# print('abc'.isalpha())
# print('abc244'.isalnum())
# print(" jdhdj ".strip())
# print(" jdhdj ".lstrip(),"djdjd")
# print(" jdhdj ".rstrip(),"sdhf", sep='-')
# print(course.startswith("Py"))
# print(course.endswith("stack"))

print(course.replace("Python", "Javascript"))
print(course.split(' '))
print(course.split('t'))
print(" ".join(["hello","world"]))
print("Name:",name,"\nCourse:",course)