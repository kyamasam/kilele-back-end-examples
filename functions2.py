studentDetails ={
    "name": "Sam",
    "email": "samield@gmail.com",
    "phone": "+25481828123"
}
studentDetails2 ={
    "name": "Victor",
    "email": "victor@gmail.com",
    "phone": "+254811228123"
}


def showStudentDetails(studentData: dict ):
    """
    This function shows student details
    
    studentData : Disctionary with keys :
        name: str
    """
    print(studentData['name'])
    print(studentData['email'])
    print(studentData['phone'])


showStudentDetails(studentDetails)
showStudentDetails(studentDetails2)



def detailedStudentInformation(email, phone, name="Samuel"):
    print("name " + name)
    print("email " +email)
    print("phone " + phone)


detailedStudentInformation(name="Peter", email="peter@gmail.com",  phone="2547126612")

print("\n \n\n \n")

def sqr(num:int) -> int:
   " Returns the square of a number"
   return num*num

my_sqr = sqr(12)
print(my_sqr)


# arguments vs parameters



def sum_of_numbers(*nums):
    total = 0
    for i in nums:
        total+=i
    return total

print(sum_of_numbers(12, 13, 12,12))



# multiple key work arguments

def detailedStudentInformation(**kwargs):
    # email = details.pop('email', None)
    # print("name " + details['name'])
    # if email is not None:
    #     print("email " + email)
    # print("phone " +  details['phone'])

    ## dict keys
    for key in dict.keys(kwargs):
        print(key + " " +  kwargs[key])

detailedStudentInformation(name="sam", email="sam@gmail.com",  phone="2547172812",dorm= "Dorm 1")


def bark():
    pass

bark()