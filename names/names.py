import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Starter solution: runtime complexity O(n**2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# MVP solution
# names_one = {name: 1 for name in names_1}

# duplicates = []
# for name_2 in names_2:
#     if name_2 in names_one:
#         duplicates.append(name_2)

# BST solution
# duplicates = []
# names_1_tree = BinarySearchTree(names_1[0])
# for i in range(1, len(names_1)):
#     names_1_tree.insert(names_1[i])
# for name in names_2:
#     if names_1_tree.contains(name):
#         duplicates.append(name)

# Stretch solution
duplicates = []
names_1.sort()
names_2.sort()
index_1 = 0
index_2 = 0
while index_1 < len(names_1) and index_2 < len(names_2):
    if names_1[index_1] == names_2[index_2]:
        duplicates.append(names_1[index_1])
        index_1 += 1
        index_2 += 1
    elif names_1[index_1] <= names_2[index_2]:
        index_1 += 1
    else:
        index_2 += 1

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
