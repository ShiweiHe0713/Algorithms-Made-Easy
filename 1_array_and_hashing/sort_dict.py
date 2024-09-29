my_dict = {(2, 3): 'a', (1, 4): 'b', (3, 2): 'c'}

# sort first by first element in key, then sort by the second element

my_dict = dict(sorted(my_dict.items(), key=lambda item: (item[0][0], item[0][1])))

print(my_dict)