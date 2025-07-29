
# ============= >  Function  < ===============

# def Display():
#     print("Hello World")

# call the display function 
# Display()
# Display()
# Display()
# Display()
# Display()
# Display()
# Display()
# Display()
# Display()

# for i in range(10):
#     Display()

# ========== > Function Parameters < ============

# def Display_Name (name):
#     print("Hello, ", name) 


# call the display_name function 
# Display_Name("Ishfaq")
# Display_Name("Hammad")
# Display_Name("Ali")
# Display_Name("Ahmad")

# ========= > Return Values < =============

# def Addition (num1, num2) :
#     reuslt = num1 + num2
#     return reuslt

# reuslt1 = Addition(23, 25)
# print(reuslt1)

# print(Addition(45, 50))
# print(Addition(15, 50))
# print(Addition(235, 500))
# print(Addition(41, 10))

# ========== > Default parameters < ===============

# def Display (name="Ishfaq"):
#     print("Hello, ", name)


# Display("Hammad")

# x = 10 
# x = 5


# ============= > Keyword Arguments < ===============

# def Display_Student_Data (name, age):
#     print(f"Student name is {name} and student age is {age}.")


# Display_Student_Data(age=20, name="Ishfaq")

# ============= > Vataible Numbers of Arguments < =================

# ============== > non-keywords arguments < =============

# def addition (*num):
#     total = sum(num)
#     return total 

# print(addition(10, 20, 30, 40, 50))

# ============ > keywords arguments < =============

# def Display_Student_Data (**info) :
#     for key, value in info.items():  # [(key, value), (key. value), (key, value)]
#         print(f"Key : {key} and value : {value}")


# Display_Student_Data(name="Ishfaq", age=20, country="Pakistan")


# ======== > Scope of the variables < ==============

# student_marks = 30

# def Display_Student_Marks (Marks):
#     student_Num = Marks
#     global x 
#     x = 25
#     print("Local Varibale Student Marks : ", student_Num)
#     print("Global Variable Student Marks : ", student_marks)


# # call the function
# Display_Student_Marks(student_marks)

# print(x)

# ============ > Lambda Function < ============

# def square (x):
#     return x*x

# square = lambda x: x*x

# print(square(6))

# ============ > Docstring < ==========

# def Display ():
#     """This function display string."""
#     print("Hello World")

# print(Display())
# print(Display.__doc__)