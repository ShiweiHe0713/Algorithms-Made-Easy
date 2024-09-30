my_dict = {(2, 4): 'a', (2, 3): 'b', (3, 2): 'c'}

# sort first by first element in key, then sort by the second element

my_dict = dict(sorted(my_dict.items(), key=lambda item: (item[0][1], item[0][0])))

print(my_dict)