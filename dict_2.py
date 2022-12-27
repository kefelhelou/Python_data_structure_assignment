# 2: Delete a list of keys from a dictionary
# Given:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# # Keys to remove
# keys = ["name", "salary"]
# Expected output:
# {'city': 'New york', 'age': 25}

####### SOLUTION #######

sample_dict = {
     "name": "Kelly",
     "age": 25,
     "salary": 8000,
     "city": "New york"
 }

print("The dictionary before removing any item:", sample_dict)

sample_dict.pop("name")
sample_dict.pop("salary")

print("The dictionary after removing any item:", sample_dict)
