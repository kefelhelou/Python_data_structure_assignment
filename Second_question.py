# 2_ Use else block to display a message “Done” after successful execution of for loop
# For example, the following loop will execute without any error.
# Given:
# for i in range(5):
#     print(i)
#
# Expected output:
# 0
# 1
# 2
# 3
# 4
# Done!

####### SOLUTION #######

x = int(input("Enter the number :  "))
for i in range(x):
    print("#" , i)
print("# Done !")