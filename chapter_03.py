
age = 17 

# ============ > if statement < ==============

# if age >= 18:
#     print("you are eligible for the vote.")

# ============ > if-else statement < ==============

# if age >= 18 :
#     print("you are eligible for the vote.")
# else :
#     print("you are not eligible for the vote.")


# =========== > if_elif_else statement <===================

# math_marks = 61

# if math_marks >= 90:
#     print("Grade : A")
# elif math_marks >= 80:
#     print("Grade : B")
# elif math_marks >= 70:
#     print("Grade : C")
# elif math_marks >= 60:
#     print("Grade : D")
# else :
#     print("Grade : F")
    

# ======== > Nested COndition < ==========

# age = 18 
# citizen = "Pakistan"

# if age >= 18:
#     if citizen == "Pakistan":
#         print("You can vote.")
#     else :
#         print("only citizens can vote.")
# else:
#     print("you must be 18 or older to vote.")

# ============ > Match Case Statement < =============

a = 10
b = 20

c = a + b 

match c:
    case 10:
        print("answer is 10")
    case 20:
        print("answer is 20")
    case 30:
        print("answer is 30")
    case _:
        print("answer not match")