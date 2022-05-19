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
