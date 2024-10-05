mydict = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}

# # Print Dict
# print("Dictionary : " , mydict)

# # Length:
# print(len(mydict))

# # Print using Index:
# print(mydict["name"])

# # Access Items
# age = mydict.get("age")
# print("Age is " , age)

# # Get Keys and Set Keys
# x = mydict.keys()
# print(x)
# mydict['mobile'] = 1257848
# print(x)

# # Get Values and Set Values
# x = mydict.values()
# print(x)
# mydict['mobile'] = "Hello"
# print(x)

# # Get Items : The items() method will return each item in a dictionary, as tuples in a list
# x = mydict.items()
# print(x)

# # Check if Key Exists
# if "name" in mydict:
#     print("name key exists")
# else:
#     print("name key doesn't exists")

# # Update Method
# print("Before Update : " , mydict)
# mydict.update({"age" : 45})
# print("After Update : " , mydict)

# # Add Item : The update() method will update the dictionary with the items from a given argument.
#  If the item does not exist, the item will be added.

# # Delete Item
# 1.pop() method
# mydict.pop("age")
# print(mydict)

# 2.del keyword
# del mydict["age"]
# print(mydict)

# 3.popitem() method :The popitem() method removes the last inserted item
# mydict.popitem()
# print(mydict)

# 4.clear() method
# mydict.clear()
# print(mydict)

# 5.del whole dict
# del mydict

# # Looping
# for x in mydict:
#     print(x , " -> " , mydict[x])

# # Looping using values
# for x  in mydict.values():
#     print(x)

# # Looping using keys
# for x  in mydict.keys():
#     print(x)

# # Looping using items()
# for x , y in mydict.items():
#     print(x , " -> " , y)

# # Copy Dictionary : copy()
# x = mydict.copy()
# print(x)

# # Copy Dictionary : dict()
# y = dict(mydict)
# print(y)

# # Nested Dictionaries Method-1
# myfamily = {
#     "child1" : {
#         "name" : "Emil",
#         "year" : 2004
#     },
#     "child2" : {
#         "name" : "Tobias",
#         "year" : 2007
#     },
#     "child3" : {
#         "name" : "Linus",
#         "year" : 2011
#     }
# }
# print(myfamily)

# # Nested Dictionaries method-2
# child1 = {
#     "name" : "Emil",
#     "year" : 2004
# }
# child2 = {
#     "name" : "Tobias",
#     "year" : 2007
# }

# myfamily = {
#     "child1" : child1,
#     "child2" : child2
# }
# print(myfamily)

# # Access items of Nested Dictionaries
# print("child 1 Name : " , myfamily["child1"]["name"])

# # fromKeys function : Returns a dictionary with the specified keys and value
# Syntax : dict.fromkeys(keys, value)
# x = ('key1' , 'key2' , 'key3')
# y = 0
# dicts = mydict.fromkeys(x,y)
# print(dicts)

# # zip : means assign new values to new keys
# x = ('key1' , 'key2' , 'key3')
# y = (0,1 , 10)
# dicts = dict(zip(x,y))
# print(dicts)
