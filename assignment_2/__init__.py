# question 1
# Return all the duplicate value list of arraylist s from
# Input:
# [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
# Output:
# 1 -> 2
# 8 -> 2
# 0 -> 3, 4 -> 2

def get_duplicates(input_list):
    duplicates = []
    for list_item in input_list:
        if input_list.count(list_item) > 1:
            if duplicates.count(list_item) == 0:
                duplicates.append(list_item)

    return duplicates


# numbers = [1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7]
# duplicates_items = get_duplicates(numbers)
# print("Duplicates Items :-", duplicates_items)

# question 2
# Merge two lists
def merge_list(list1, list2):
    new_list = []
    # assume that length of both lists are equal
    for index in range(len(list1)):
        new_item = list1[index] + " " + list2[index]
        new_list.append(new_item)
    return new_list


# list1 = ["a", "c"]
# list2 = ["b", "d"]
# mergedList = merge_list(list1, list2)
# print("Merged list is  :-", mergedList)

# question 3
# Given a nested list extend it by adding the
# sub list ["h", "i", "j"] in such a way that it
# will look like the following list
def add_in_nested_list():
    given_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    add = ["h", "i", "j"]
    given_list[2][1][2].extend(add)
    print(given_list)


# add_in_nested_list()

# question 4
# Map the dictionary in the following manner
# Keys = [‘Ten’, ‘Twenty’, ‘Thirty’]
# Value = [10,20,30]

def create_map_ascending(key, value):
    # assume that length of both lists are equal
    dict = {}

    for index in range(len(key)):
        mapped = map(key[index], value[index])
        dict.update(mapped)

    print(dict)


# keys = ['Ten', 'Twenty', 'Thirty']
# value = [10, 20, 30]
# create_map_ascending(keys, value)


# question 5
# Merge following two Python dictionaries into one

def merge_map(dict1, dict2):
    dict3 = dict1.copy()

    for key, value in dict2.items():
        dict3[key] = value
    print(dict3)


# given_dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# given_dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
# merge_map(given_dict1, given_dict2)

# question 6
# Rename key city to location in the following dictionary
def rename_key(dict, oldKey, newKey):
    dict[newKey] = dict.pop(oldKey)
    print(dict)


# sampleDict = {
#   "name": "Kelly",
#   "age": 25,
#   "salary": 8000,
#   "city": "New york"
# }

# oldKey = "city"
# newKey = "location"
# rename_key(sampleDict, oldKey, newKey)

# question 7
# Convert Dictionary to list
# The original dictionary is : {‘HuEx: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4, 5]}
# The converted list is : [[‘HuEx, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]
def dict_to_list(input_dict):
    new_dict = list(input_dict.items())
    print(new_dict)

# given_dict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# dict_to_list(given_dict)
