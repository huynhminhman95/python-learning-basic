my_list = [1, 2, 3, 4]
# for loop
#
# for item in range(len(my_list)):
#     print(f"{item} : {my_list[item]}")

# while loop
# count = 1
# while counts < 5:
#     print("Hello, how arw you?")
#     count += 1

# break, continue in loop
for item in my_list:
    print(item)
    if item != 3:
        continue
    break
