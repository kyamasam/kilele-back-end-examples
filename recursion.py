
# total =0
# counter = 0
# def sum(num, number_of_times ):
#     global total
#     global counter
#     total = total+num
#     print("total", total)
#     counter= counter+1 
#     print(" this function has run " +str(counter) +" times")
#     if counter < number_of_times:
#         sum(num, number_of_times)
#     return total

# print(sum(12, 6))

# number x 
# add x by itself 5 times 

# factorial of 4
# 4*3
# 4*2
# 4*1

def factorial(num):
    if num== 0: 
        return 1
    else:
        return num * factorial(num-1)
    

 
