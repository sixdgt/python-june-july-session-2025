# dictionary in python -> stores data in key-value pair
player_detail = {
    "name": "Rohit Poudel",
    "country": "Nepal",
    "age": 24,
    "position": "National Team Captain"
}

print(player_detail)
print(type(player_detail))

print("items of dict: ", player_detail.items())
for key, value in player_detail.items():
    print("Keys: ", key, " Values: ", value)

print("Keys of dict: ", player_detail.keys())
print("Values of dict: ", player_detail.values())
# clear() - removes all items from a dict
# copy() - make a copy of dict
# setdefault() - to add new key-value pair or update key-value pair
product = {
    'title': 'Wireless MIC',
    'price': 1500.00,
    'category': 'Electronics',
    'brand': 'Fantech'
}

print("product details: ", product)
# adding new item with key-value
product.setdefault('model', 'XM12') # 1st argument is key and 2nd argument is value
print("product details after adding: ", product)
# if we pass single argument only: in such case the value is set as null i.e None
product.setdefault('quantity')
print("product details after adding key only: ", product)
# what if we add key-value with existing key
product.setdefault('brand', 'Samsung')
print("product details after adding exising key with new value: ", product) # will do nothing
# update() - update new key-value pair
product.update({'brand': 'Samsung'}) # updating brand
print("product details after update: ", product)

# passing new key-value & existing key-value
product.update({'quantity': 8, 'color': 'Material Black', 'brand': 'Shure', 'build_quality': 'Plastic Made'})
# dict is mutable so it will update the existing variable/object
print("product details after multiple items update: ", product)
# fromkeys() - creates new dict with sequences
# pop(key) - removes specific item with passed key
# popitem() - removes last inserted item and returns keyvalue


# str is immutable so it creates new reference when we try to change 
msg = "I am from Kathmandu, Nepal."
# tuple same as str it is also immutable
# upper() and lower() - convert string to uppercase or lowercase
print("msg before: ", msg)
print("Uppercase:", msg.upper())
print("msg after: ", msg)

# set methods
# un-order sequence that means elements are stored in random order
# so no indexing of elements
set_fruits = {'banana', 'apple', 'cherry', 'orange', 'mango'}
print("set of fruits: ", set_fruits)
set_fruits.pop()
print("set of fruits after pop: ", set_fruits)
set_fruits.pop()
print("set of fruits after pop: ", set_fruits)

set_A = {1, 2, 3, 4, 5, 6, 7, 8, 9} # whole number
set_B = {2, 4, 6, 8 , 10, 12, 14} # even number
set_C = {1, 3, 5, 7, 9, 11, 13, 15} # odd number
# difference of whole - even : will change affect/change the original sets
print("Set A before: ", set_A)
print("Set B before: ", set_B)
set_A_diff_set_B = set_A.difference(set_B)
print(set_A_diff_set_B)
print("Set A after: ", set_A)
print("Set B after: ", set_B)

# in case of difference_update
print("Set A before: ", set_A)
print("Set B before: ", set_B)
set_A_diff_set_B_i = set_A.difference_update(set_B) # will remove all matched elements from set A but no change in setB
print(set_A_diff_set_B_i)
print("Set A after: ", set_A)
print("Set B after: ", set_B)
set_A = {1, 2, 3, 4, 5, 6, 7, 8, 9} # whole number
set_B = {2, 4, 6, 8 , 10, 12, 14} # even number
set_C = {1, 3, 5, 7, 9, 11, 13, 15} # odd number

print("Set A before: ", set_A)
print("Set B before: ", set_B)
set_B_diff_set_A_i = set_B.difference_update(set_A) # will remove all matched elements from set B but no change in setA
print(set_B_diff_set_A_i)
print("Set A after: ", set_A)
print("Set B after: ", set_B)

# symmetric_difference
set_A = {1, 2, 3, 4, 5, 6, 7, 8, 9} # whole number
set_C = {1, 3, 5, 7, 9, 11, 13, 15} # odd number
# difference of whole - even : will change affect/change the original sets
print("Set A before: ", set_A)
print("Set C before: ", set_C)
set_A_diff_set_C = set_A.symmetric_difference(set_C)
print(set_A_diff_set_C)
print("Set A after: ", set_A)
print("Set C after: ", set_C)
# symmetric_difference_update
print("Set A before: ", set_A)
print("Set C before: ", set_C)
set_A_diff_set_C = set_A.symmetric_difference_update(set_C) #Set A will update with remaing elements of both Set A & C
print(set_A_diff_set_C) # here it will change the existing set and will return None
print("Set A after: ", set_A)
print("Set C after: ", set_C)

# task: practice the remaining methods of list, str, tuple, dict, set

# lamda function or anonymous function -> nameless function
def sum(a, b):
    return a + b

print(sum(12, 45))

addition = lambda x, y : x + y
print(addition(5, 6))
data = []
for i in range(10):
    data.append(sum(i , i + 1))

print(data)
# map() takes two parameter : 1st argument function & 2nd argument iterable 
result = list(map(lambda x: x + 5, range(10)))
print(result)