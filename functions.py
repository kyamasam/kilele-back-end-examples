# student_name = "Victor"

# print("Hello world! "+student_name)

# student_name2 = "Jose"
# print("Hello world! "+student_name2)


# define the function
def print_student(school_name, student_name="Peter"):
    print("student is "+student_name + " and he attends "+school_name)

# call the function
print_student(school_name ="SPU")
print_student("Jose", "Kilele")


# passing list as argument

games = ["hokey", "basketball", "football", "Swimming"]

def print_student_details(student_name, student_games):
    print("student "+ student_name+" plays " )

    for count in range(len(student_games)):
        print(str(count +1) + '. ' + str(student_games[count]))

print_student_details("Victor",  games)

# define function
def sum_and_square(num1, num2):
    sum = num1+num2
    sqr = sum * sum
    print(sqr)

# call/execute function
sum_and_square(12, 3)
sum_and_square(24, 4)
sum_and_square(12, 1)



def sqr_and_sum_lst(num1, num2, num3, num4, num5):
    sum = num1+num2 + num3 + num4 + num5
    sqr = sum * sum
    print(sqr)

sqr_and_sum_lst(12, 22, 45, 16, 18)

# passing a list as an parameter
def sqr_and_sum_lst_comp(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    sqr = sum * sum
    print(sqr)

my_list = [12, 22, 45, 16, 18]
sqr_and_sum_lst_comp(my_list)


# for loops
my_names = ["sam", "kymama", "muasya"]

for i in range(len(my_names)):
    print(my_names[i])
# return types


def multiply_numbers(num1, num2):
    multiplication = num1*num2
    return multiplication

result = multiply_numbers(12, 2)

print("the result of multiplication is " +str(result))

total_money = multiply_numbers(150, 10)

print(" total cash in kes is " + str(total_money))


# assignment
# convert the rock_paper scissors game to use functions