studentList = ["davis", "Washington", "Alex", "Peter"]
# 0, 1, 2
studentNumber = len(studentList)
# print(studentList[studentNumber -1])

fruits = list(["banana", 200, "orange", 300, True, "yes"])
#                -6     -5      -4      -3     -2    -1
print(fruits)

if 200 in fruits:
    print(" 200 is in fruits")
else:
    print(" 200 is not in fruits")

fruits[1] = "orange"

print(fruits)

fruits.append(10)

print(fruits)

fruits[1:3] = [True, True]

print(fruits)

fruits.insert(0,"Papai")

print(fruits)
