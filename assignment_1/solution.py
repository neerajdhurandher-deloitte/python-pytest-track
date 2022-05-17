# Problem 1
# create a class with name StringClass which should take string
# as an input from constructor. It should have method which
# should return the length of the string and a method to convert
# string to list of characters. This method will take an
# argument as string to convert.
from collections import Counter


class StringClass:

    def __init__(self, inputString):
        self.string = inputString

    def lengthOfString(self):
        return len(self.string)

    def str2listConverter(self, inputStr):
        return [char for char in inputStr]

stringClass = StringClass("hello")
print("length of the string :- ", stringClass.lengthOfString())
print("String converted to list : - ", stringClass.str2listConverter("HashedIn"))


# Problem 2
# Create class PairsPossible which should inherit from StringClass
# and should have a method for storing list of all possible pairs formed.
# It should also have a method to print list of every possible pair in
# same line but with space between them. Pairs should be in list.

class PairsPossible(StringClass):
    def pairs(self):
        list = []

        list1 = StringClass.str2listConverter(self,self.string)
        for i in range(0,len(list1)):
            temp = ""
            for j in range(i+1,len(list1)):
                temp = list1[i]+list1[j]
                list.append(temp)
        return list

pairPossible = PairsPossible("hello")
print("all possible pairs are :- ", pairPossible.pairs())

# Problem 3
# Create a class SearchCommonElements which should take up a string.
# Your task is to create a method to find common elements from string
# taken in StringClass and string taken in PairsPossible class and
# return the answer in list. Note- Please use dictionary logic to
# find common elements.
class SearchCommonElements(StringClass):

    def commonElements(self):
        d = dict(Counter(list(self.string)))
        res = []
        for j in d:
            if d[j] >= 2:
                res.append(j)
        return res

searchCommonElements = SearchCommonElements("asdfdsasdsasd")
print("Common elements are :- ", searchCommonElements.commonElements())