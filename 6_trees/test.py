from collections import defaultdict

table = defaultdict(list)
table2 = {}

table[1] = 3
table[2] = 6
table[-3] = 7

table2[1] = 3
table2[2] = 6
table2[-3] = 7

# print keys only
for i in table.keys():
    print(i)

# print values only
for i in table.values():
    print(i)

# print key, val pair
for key, val in table.items():
    print(key, val)

