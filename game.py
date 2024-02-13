# username = input("Enter username:")
# print("username is "+ username)


games =["Basketball", "Swimming",  "Football"]
subjects =["Math", "Enf",  "Sci"]
students =["Kilia", "Esterh",  "Kelsie"]


"""


 From the program you created earlier, 
 suppose the head master wanted to know at a 
 glance each student's name, what game(just a single game per student) 
 they play, the subject(1) they take and what 
 they scored. Create a program that can store this 
 information and display it.

"""
student1 = {
    "name": "killian", "subject":"Math", "game":"basketball", "score":10
}
student2 = {
    "name": "Kelsie", "subject":"Eng", "game":"basketball", "score":70
}

# print(student2["name"])

students_info =  [
    {
     "name": "kalian", "subject":"Math", "game":"basketball", "score":10
    },
    {
     "name": "Kellie", "subject":"Eng", "game":"basketball", "score":70
    }
]

# print(students_info[1]['name'])


numbers = [12, 13, 123]

# for number in numbers:
#     print(number)

for student in students_info:
    print(""+student['name'] + " studies " +student["subject"]+" plays "+student["game"] + " and scored " + str(student['score']))
    print()



username = input("Enter your name:")
age = input("Enter your age:")
class_name = input("enter your class")

print(" your name is "+ username + " and your age is "+ age)


