
# ======== > Types of the errors < ==========

# ======= > Syntax Error < =========

# if x <= 20 
#     print("x is the smaller than 20")

# ========== > Runtime Error < ==========

# a = 10/0
# print(a)

# ========== > Try and Except Block < =========

# try:
#     num = int(input("Enter the Number : "))
#     reuslt = 20/num
#     print("Reuslt : ", reuslt)
# except ZeroDivisionError:
#     print("Cannot Divided by Zero")
# except ValueError:
#     print("Invalid value, please enter the number instead of zero or string")
# # finally :
# #     print("Execution Finished")
# else:
#     print("Your Entered Number : ", num)


# x = 20 
# print(x)

# ======== > Rasing Execptions < =============

# age = int(input("Enter the age : "))

# if age <= 0:
#     raise ValueError("Age cannot be negative")

# x = 20
# print(x)

# ====== > Custom Error Message < =========
try:
    age = int(input("Enter the age : "))

    if age <= 0:
        raise Exception("Age cannot be negative")
except Exception as e:
    print("Error: ", Exception)


x = 20
print(x)