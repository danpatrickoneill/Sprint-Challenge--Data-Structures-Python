import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Original search code: runtime complexity O(n**2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Using BST
names_1_bst = BinarySearchTree(names_1[0])
for name in names_1:
    names_1_bst.insert(name)

duplicates = []
for name_2 in names_2:
    if names_1_bst.contains(name_2):
        duplicates.append(name_2)

# Seems to be faster, but less in the spirit of the lessons of the week
# names_1_dict = {name: True for name in names_1}

# duplicates = []
# for name_2 in names_2:
#     if name_2 in names_1_dict:
#         duplicates.append(name_2)

# Lists only
# Not sure yet!


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
