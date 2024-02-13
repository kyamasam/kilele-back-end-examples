# student = {
#     "level": 2,
#     "subject":'flusk',
# }

# if student["level"] == 2:
#     print("student is  learning" + student['subject'])
# else:
#     print("student level does not exist" )

# print("student is  learning" + student['subject']) if student["level"] == 2 else     print("student level does not exist" )

# if student["level"] == 2: print("student is  learning" + student['subject'])


# a = 12
# b = 10
# if (a > b) and a< 10:
#     print(str(a)+" is greater than"+ str(b)+ " and less than 10")
# elif (a>b)  and a > 10:
#     print(str(a) + " is greater than "+ str(b)+ " and greater than 10")
# else:
#     print(str(b)+ " is greater than " + str(a))

#print("a is greater than b") if a > b else print("b is less than a")
# print("A") if a > b else print("B")


# lists 



students = ['student1', 'student2', 1, 4]
students2 = ['student3']
students.append(12)
print(students)

students3 = students + students2

print(students3)

studentName = 'kyama'
#dictionaries

studentDetails = {
    "name":"ian",
    "level":1,
    "subject":'python'
}

print(studentDetails['name'] +" is in " + str(studentDetails['level']) + " and is studying " + studentDetails['subject'])

# sets 

studentNumbers = {
    12, 13, 34
}
studentNumbers2 ={
    12, 11, 15
}
studentNumbers3 =[
   14, 12, 13
]

print(studentNumbers.union(studentNumbers2))
print(studentNumbers.intersection(studentNumbers2))
print(studentNumbers.symmetric_difference(studentNumbers2))

print(sorted(studentNumbers))



# tuples

studentNumbers4 = (12, 24, 14)

studentNumbers5 = (15, 27, 14)

studentNumbers6 = studentNumbers4 + studentNumbers5

print(studentNumbers6)



### 

a = 12
b= 11

if a>b:
    print("a is greater than b")
elif a == 12:
    print("a is 12")
elif b == 12:
    print("a is 12")
else:
    print("not equals")


# ternary operators 
    
print("a is greater than b") if (a > b and a ==12) else print("a is les than b")

z = ""

if a > b:
    z = "a is greater than b"
else:
    z = "b is greater than a"

z = "a is greater than b" if a > b else "b is greater than a"