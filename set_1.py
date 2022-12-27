# 1: Add a list of elements to a set
# Given a list, write a program to add all its elements into a given set.
# Given:
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# Expected output:
# Note: Set is unordered.
# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

####### SOLUTION #######

### THIS CODE WILL PRINT ORDER SET ###
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
#
# sample_set.update(sample_list)
#
# print(sample_set)

### THIS CODE WILL PRINT UNORDERED SET ###

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

for i in sample_list:
    sample_set.add(i)

print(sample_set)

