nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []

for n in nums:
    my_list.append(n)

print(my_list)
print(nums)

# using comprehenson

my_list2 = [n for n in nums]
print(my_list2)

squared_list = [n * n for n in nums]
print(squared_list)

# conditional comprehension

even_squared_list = [n * n for n in nums if n % 2 == 0]
print(even_squared_list)


#Map and lambdas
#map and filters


# i want a (letter num) pair for each abcd and 0123

letter_num_list = [(letter, num, symbol)
                   for letter in "abcd" for num in range(4) for symbol in "*&@$"]
print(letter_num_list)

# dict comprehension

names = ["Tony Stark", "clark", "peter parker", "logan"]
heros = ["iron man", "super man", "spider man", "wolverine"]

hero_name_dict = {(name, hero)
                  for name, hero in zip(names, heros) if name != "logan"}
print(hero_name_dict)

# set comprehension

nums = [1, 2, 2, 3, 4, 1, 5, 6, 7, 5, 8, 9, 10, 2, 3, 6, 4, 2]

num_set = {num for num in nums}
print(num_set)


#generator comprehension -- discuss later