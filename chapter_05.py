
# age = 20

# ishfaq_student_Marks = 10.5,20,25,18,NaN

# ======= > List < =========

# fruits = ["apple", "mango", "banana"]

# print(fruits[-1])

# fruits[1] = "orange"

# print(fruits)

# fruits.append("grape") #add at end

# print(fruits)

# fruits.insert(1, "kiwi") # add at positoin 1

# print(fruits)

# fruits.remove("apple") # remove value in the list

# print(fruits)

# fruits.pop() # remove last item 

# print(fruits)

# print(len(fruits)) # check the no of values in the list 

# ======== > List comprehension < ==========

# squares = [ x*x for x in range(20)] 
# print(squares)

# even_numbers = [x for x in range(100) if x % 2 == 0]
# print(even_numbers)

# ========== > Tuples < ==============

# colors = ("red", "green", "blue")
# print(colors[1])

# # colors[0] = "orange"
# # print(colors)

# Student_data = ("Ishfaq", 20, "Pakistan")

# name, age, country = Student_data

# print(f"Name: {name}, Age: {age}, Country: {country}")

# ======== > Sets < ===========

# numbers = {1, 2, 3, 4, 5, 5, 5, 2, 4, 6}

# # numbers.add(111)
# numbers.update([33, 34, 35])
# # numbers.remove(100)
# numbers.discard(100)

# print(numbers)

# set1 = {1, 2, 3, 4, 4, 2, 1}
# set2 = {2, 5, 6, 7}

# print("Union : ", set1.union(set2))
# print("Intersection : ", set1.intersection(set2))
# print("Difference: ", set1.difference(set2))


# ========== > Dictionary < ===============

# Student_Data = {
#     "name" : "Ishfaq",
#     "age" : 25,
#     "country" : "Pakistan"
# }

# # print(Student_Data["name"])

# Student_Data["age"] = 20
# Student_Data["city"] = "Trag"

# # print(Student_Data)
# # print(Student_Data.keys())
# # print(Student_Data.values())
# print(Student_Data.items())

# list_dict_keys = list(Student_Data.keys())
# print(list_dict_keys)

# tuple_dict_keys = tuple(Student_Data.keys())
# print(tuple_dict_keys)

# Student_Data.clear()
# print(Student_Data)

# =========== > Nested Dictionary < =========

Students = {
    "Student1_data" : {"name" : "ishfaq", "age" : 20},
    "Student2_data" : {"name" : "ali", "age" : 25}
}

Students["Student1_data"]["name"] = "Hammad"

print(Students["Student1_data"]["name"])
print(Students["Student1_data"].keys())