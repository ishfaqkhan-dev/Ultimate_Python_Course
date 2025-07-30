
# ======== > Opening and Reading a file < ==========

# file = open("text1.txt", "r")
# content = file.read()
# print(content)
# file.close()

# ========= > Writing to a file < ============

# file = open("text1.txt", "w")
# file.write("\nThis is my new line.")
# file.close()

# ========= > Append Mode < ================

# file = open("text1.txt", "a")
# file.write("\nThis is my new line.")
# file.close()

# ========== > Reading line by line <==============

# file = open ("text1.txt", "r")
# content = file.read()
# print(content)
# file.close()

# for line in file:
#     print(line.strip())

# file.close()

# ======== > With Statement < =============

# with open("text2.txt", "r+") as file :
#     content = file.read()
#     print(content)
#     file.write("\n This is my new line.")

# print("file closed automatically.")

# ========= > Working with csv < ===========

import csv

# writing csv
# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","age"])
#     writer.writerow(["Ali",20])
#     writer.writerow(["sara","22"])

with open("data.csv", "r") as file1:
    Content = csv.reader(file1)
    for row in Content:
        print(row)