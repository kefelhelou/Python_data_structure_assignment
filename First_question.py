# 1- Display numbers from a list using a loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# ●	The number must be divisible by five
# ●	If the number is greater than 150, then skip it and move to the next number
# ●	If the number is greater than 500, then stop the loop
# Given:
# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# Expected output:
# 75
# 150
# 145

####### SOLUTION #######


numbers = [12, 75, 150, 180, 145, 525, 50]
new_numbers = []

for i in numbers:
    if i > 150:
        if i > 500:
            break
        continue
    if i % 5 == 0:
        new_numbers.append(i)

print(new_numbers)