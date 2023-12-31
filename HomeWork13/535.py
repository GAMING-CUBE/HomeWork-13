list = [10, 5, 11, 2, 3, 5, 8, 9, 3, 4, 2]

new_list = set(list)
new_list = sorted(new_list)

for i in range(len(new_list)):
    print(new_list[i], end=" ")
