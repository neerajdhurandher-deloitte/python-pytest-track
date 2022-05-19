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

